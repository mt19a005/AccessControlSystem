# AccessControlSystem

部屋の入退出処理を行う。

## Description

- 顔写真撮影処理
1. RTSPによって、カメラから映像を送信
1. 動体認識したらキャプチャ（以降、画像A）し、ディレクトリ"Test"に画像を保存。

- 顔推定処理
1. Testにファイルが有るか確認
1. ファイル読み込み(画像A)
1. 画像Aのカスケード領域を切り取り、画像Bに貼り付け。
1. 顔推定アルゴリズムによって、画像Bの顔推定
1. 推定された人の名前をファイル'sojourner.txt'に書き込み
1. 画像Bをディレクトリ"Train"に追加
1. 1~5を繰り返す。

- 退室処理
1. 後々

## Reference
- RTSP
https://qiita.com/haseshin/items/59aed8bae8a1fa88fa21
- カスケード
https://qiita.com/hitomatagi/items/04b1b26c1bc2e8081427
- 顔推定
https://qiita.com/hitomatagi/items/8f2f37646179aca68649
- 顔データベース(yale-face)
http://vision.ucsd.edu/content/yale-face-database

## Requirement
* Python 3.8.4
## Author
Motoharu Taguwa
