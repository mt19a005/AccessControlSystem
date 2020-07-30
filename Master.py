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

for key, value in Data.Name.items():
    print(key, ", ", value)

# トレーニング実施
Recognizer.train()

# -   -   -   -   テスト画像追加    -   -   -   - #
testPath = "./Test/"

while(1):
    # testフォルダに画像がある場合の処理
    if len(os.listdir(testPath)) > 0:
        # 戻り値 :　顔アップの画像郡
        testImages, _ = Recognizer.getImgData(testPath, os.listdir(testPath)[0])
        # 名前をつけてtrainへ保存

        # 画像1枚ずつ処理
        i = 0
        while i < len(testImages):
            recognizedLabel = Recognizer.recognize(testImages[i])
            #  trainData.imagesに保存
            Data.trainData.images.append(testImages[i])
            #  trainData.labelsに保存
            Data.trainData.labels.append(recognizedLabel)
            # テスト画像をtrainフォルダに保存
            for key, value in Data.Name.items():
                if str(recognizedLabel) == key:
                    # trainフォルダに保存する命名規則の番号を増やす
                    Data.Name[key] += 1

                    name = trainPath + str(recognizedLabel) + "-" +  str(Data.Name[key]) + ".png"
                    cv2.imwrite(name, testImages[i])
                    print(name)
            i+=1

        # トレーニング
        Recognizer.train()
