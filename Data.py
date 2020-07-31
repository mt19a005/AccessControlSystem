# データ
import os

# 命名規則の番号
Name = {
    # 田桑
    "0": 0, 
    # 誰か
    "1": 0, 
    # anybody
    "2": 0,
    }

class TrainData():
    # 画像を格納する配列
    images = []
    # ラベルを格納する配列
    labels = []

# printの色変更
class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'