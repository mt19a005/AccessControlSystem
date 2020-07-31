# トレインデータを顔アップの画像にする

import cv2
import os
import numpy as np

cascadePath = "haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

srcDirPath = "./Train元画像/"
saveDirPath = "./Train顔領域/"

# 画像の番号
id = 0
# 画像の枚数
num = 0

def makeTrainROIImg(srcDirPath, saveDirPath, fileName):

    images = []
    labels = []
    global num
    imgPath = os.path.join(srcDirPath, fileName)
    saveImgPath = os.path.join(saveDirPath, fileName)
    # グレースケール
    imgSrc = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    # カスケードで顔検知
    faces = faceCascade.detectMultiScale(imgSrc, scaleFactor=1.1, minNeighbors=2, minSize=(50, 50))
    print(fileName,", ", num, " = ", len(faces))
    # 検出した顔（複数）の領域の処理
    for (x, y, w, h) in faces:
        # 顔領域を取得して200x200(pix)にリサイズ
        ROI = cv2.resize(imgSrc[y: y + h, x: x + w], (200, 200), interpolation=cv2.INTER_LINEAR)
        # ROI = cv2.resize(imgSrc[y - 50 : y + h + 50, x - 50 : x + w + 50], (200, 200), interpolation=cv2.INTER_LINEAR)
        name = saveDirPath + str(id) + "-" +  str(num) + ".png"
        cv2.imwrite(name, ROI)
        num+= 1


for fileName in os.listdir(srcDirPath):
    makeTrainROIImg(srcDirPath, saveDirPath, fileName)