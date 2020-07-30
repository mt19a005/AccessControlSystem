# マスター

import os   
import Recognizer
import Data
import cv2
import numpy as np

# -   -   -   -   初期化    -   -   -   - #
trainPath = "./Train/"
# トレイン画像を初期化
for fileName in os.listdir(trainPath):
    # カスケード処理した画像, ラベル
    trainImages, trainLabels = Recognizer.getImgData(trainPath, fileName)

    # 画像1枚ずつ処理
    i = 0
    while i < len(trainLabels):
        # TrainData.imagesに保存
        Data.TrainData.images.append(trainImages[i])
        # TrainData.labelsに保存
        Data.TrainData.labels.append(trainLabels[i])

        # trainフォルダに保存する命名規則の番号を増やす
        for key, value in Data.Name.items():
            if str(trainLabels[i]) == key:
                Data.Name[key] += 1
        i+=1



# トレーニング実施
Recognizer.train()

# -   -   -   -   !初期化    -   -   -   - #

# -   -   -   -   テスト    -   -   -   - #
testPath = "./Test/"
badConfidencePath = "./BadTest/"
while(1):
    # testフォルダに画像がある場合の処理
    if len(os.listdir(testPath)) > 0:
        #顔画像郡をとってくる。
        testImages, _ = Recognizer.getImgData(testPath, os.listdir(testPath)[0])
        # 顔が認識しなかったら
        if not testImages:
            # BadTestディレクトリに入れる
            print(Data.Color.RED + "Not detected face" + Data.Color.END)
            img = cv2.imread(testPath + os.listdir(testPath)[0])
            cv2.imwrite(badConfidencePath + os.listdir(testPath)[0], img)
            os.remove(testPath + os.listdir(testPath)[0])
            continue


        # 画像1枚ずつ処理
        i = 0
        while i < len(testImages):
            # 顔推定
            # 戻り値　label : 顔推定結果のラベル, confidence : 推定結果の信頼度
            recognizedLabel, confidenceJudge = Recognizer.recognize(testImages[i])
            if(confidence <= 50):
                print(Data.Color.GREEN + "Good confidence" + Data.Color.END)
                #  TrainData.imagesに保存
                Data.TrainData.images.append(testImages[i])
                #  TrainData.labelsに保存
                Data.TrainData.labels.append(recognizedLabel)
                # -   -   -   -   テスト画像をtrainフォルダに保存    -   -   -   - #
                # 顔推定結果のラベルと、dicの名前が一致したら、画像のナンバーを一つ増やす
                for key, value in Data.Name.items():
                    if str(recognizedLabel) == key:
                        # trainフォルダに保存する命名規則の番号を増やす
                        Data.Name[key] += 1
                        # 画像の名前を設定
                        name = trainPath + str(recognizedLabel) + "-" +  str(Data.Name[key]) + ".png"
                        # trainディレクトリに出力
                        cv2.imwrite(name, testImages[i])
                        print("TestIMG Save to \"", name, "\"")
            else:
                print(Data.Color.RED + "Bad confidence" + Data.Color.END)
                img = cv2.imread(testPath + os.listdir(testPath)[0])
                cv2.imwrite(badConfidencePath + os.listdir(testPath)[0], img)

            i+=1
        # トレーニング
        Recognizer.train()
        # テストファイルを削除
        os.remove(testPath + os.listdir(testPath)[0])
        print("Delete Test Image\n")
# -   -   -   -   !テスト    -   -   -   - #