# 画像検知

import cv2
import Data
import os
import numpy as np

# FisherFace
# recognizer = cv2.face.FisherFaceRecognizer_create()
# LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def getImgData(dirPath, fileName):
    images = []
    labels = []
    imgPath = os.path.join(dirPath, fileName)
    # グレースケール
    imgSrc = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    # カスケードで顔検知
    faces = faceCascade.detectMultiScale(imgSrc, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    if faces == ():
        return images, labels
    # 検出した顔（複数）の領域の処理
    for (x, y, w, h) in faces:
        # 顔領域を取得して200x200(pix)にリサイズ
        images.append(cv2.resize(imgSrc[y: y + h, x: x + w], (200, 200), interpolation=cv2.INTER_LINEAR))
        # ラベル
        labels.append(int(fileName[0:1]))
        # 画像を配列に格納
        return images, labels

def train():
    # トレーニング実施
    recognizer.train(Data.TrainData.images, np.array(Data.TrainData.labels))
    # トレーニング後のTrain画像枚数
    print("--- imgNum ---")
    for key, value in Data.Name.items():
        print(key, ", ", value, "Photos")

def recognize(testImage):
    # テスト画像に対して予測実施 label = 予測した人の名前, confidence = 予測的確率？
    label, confidence = recognizer.predict(testImage)
    # 予測結果をコンソール出力
    print("Predicted Label: {}, Confidence: {}".format(label, confidence))

    return label, confidence
        