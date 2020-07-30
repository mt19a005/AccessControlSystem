import cv2
import numpy as np

# cap = cv2.VideoCapture('srcMovie2.mp4')
cap = cv2.VideoCapture(0)

# 出力動画設定
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))

frame1 = cap.read()[1]
frame2 = cap.read()[1]
imgNum = 0
testPath = "./Test/"

while cap.isOpened():
    # -   -   -   -   前処理    -   -   -   - #
    # 差分
    diff = cv2.absdiff(frame1, frame2)
    # HSVのV　グレースケールよりも良い感じ
    diffV = cv2.split(cv2.cvtColor(diff, cv2.COLOR_RGB2HSV))[2]
    # メディアンフィルター（モルフォロジー変換のオープニングみたいな処理）
    diffBlur = cv2.medianBlur(diffV, 5)
    # 二値化
    diffthresh = cv2.threshold(diffBlur, 20, 255, cv2.THRESH_BINARY)[1]
    # 拡大
    diffdilated = cv2.dilate(diffthresh, None, iterations=6)
    kernel = np.ones((5,5),np.uint8)

    # -   -   -   -   前処理出力    -   -   -   - #
    cv2.imshow("diffV", diffV)
    cv2.imshow("diffBlur", diffBlur)
    cv2.imshow("diffthresh", diffthresh)
    cv2.imshow("diffdilated", diffdilated)

    # -   -   -   -   動体検出    -   -   -   - #
    contours, _ = cv2.findContours(diffdilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        # 小さい動体は除去
        if cv2.contourArea(contour) < 900:
            continue
        # # 矩形を描画
        # cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # # 動体検出
        # cv2.putText(frame1, "Detect Movement", (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        #             1, (0, 0, 255), 3)


        print("RTSPImg Save to \"", testPath + str(imgNum) + ".png"," \"")

        cv2.imwrite(testPath + str(imgNum) + ".png", frame1)
        imgNum += 1
        if imgNum == 200:
            imgNum = 0

    cv2.imshow("MOG1", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
out.release()