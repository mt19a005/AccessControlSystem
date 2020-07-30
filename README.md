# AccessControlSystem

部屋の入退出処理を行う。

## Description
1. RTSPによって、カメラから映像を送信
1. カスケードによって（もしくは、動体認識によって）、顔が認識されたらキャプチャ（以降、画像A）し、ディレクトリ"Test"に画像を保存。
1. 画像Aのカスケード領域を切り取り、画像Bに貼り付け。
1. 顔推定アルゴリズムによって、画像Bの顔推定
1. 推定された人の名前をファイル"sojourner.txt"に書き込み
1. 画像Bをディレクトリ"Train"に追加
1. 1~6を繰り返す。

退室処理は別途考える

## Requirement
* Python 3.8.4
## Author
Motoharu Taguwa