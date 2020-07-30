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
        # trainData.imagesに保存
        Data.trainData.images.append(trainImages[i])
        # trainData.labelsに保存
        Data.trainData.labels.append(trainLabels[i])

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
        # 戻り値 :　顔アップの画像郡
        a = testPath + os.listdir(testPath)[0]
        testImages, _ = Recognizer.getImgData(testPath, os.listdir(testPath)[0])

        # 画像1枚ずつ処理
        i = 0
        while i < len(testImages):
            # 顔推定
            # 戻り値　label : 顔推定結果のラベル, confidence : 推定結果の信頼度
            recognizedLabel, confidence = Recognizer.recognize(testImages[i])
            if(confidence <= 50):
                print("Good confidence")
                #  trainData.imagesに保存
                Data.trainData.images.append(testImages[i])
                #  trainData.labelsに保存
                Data.trainData.labels.append(recognizedLabel)
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
                print("Bad confidence")
                img = cv2.imread(testPath + os.listdir(testPath)[0])
                cv2.imwrite(badConfidencePath + os.listdir(testPath)[0], img)

            i+=1
        # トレーニング
        Recognizer.train()
        # テストファイルを削除
        os.remove(testPath + os.listdir(testPath)[0])
        print("Delete Test Image")
# -   -   -   -   !テスト    -   -   -   - #