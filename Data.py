# データ

import os
from enum import Enum

# 命名規則の番号
Name = {
    # 田桑
    "0": 0, 
    # 誰か
    "1": 0, 
    # anybody
    "2": 0,
    }

class trainData():
    # 画像を格納する配列
    images = []
    # ラベルを格納する配列
    labels = []