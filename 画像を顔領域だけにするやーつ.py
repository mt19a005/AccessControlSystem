# トレインデータを顔アップの画像にする

import cv2
import Data
import os
import numpy as np

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


def makeTrainROIImg(dirPath, fileName):

    images = []
    labels = []

    imgPath = os.path.join(dirPath, fileName)
    # グレースケール
    imgSrc = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    # カスケードで顔検知
    faces = faceCascade.detectMultiScale(imgSrc, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    # 検出した顔（複数）の領域の処理
    for (x, y, w, h) in faces:
        # 顔領域を取得して200x200(pix)にリサイズ
        ROI = cv2.resize(imgSrc[y: y + h, x: x + w], (200, 200), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(imgPath, ROI)

trainPath = "./Train/"

for fileName in os.listdir(trainPath):
    makeTrainROIImg(trainPath, fileName)