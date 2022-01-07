import time
from random import randrange


def changeTime():
    now_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    return now_time


def ranString(str_len: int = 8):
    contentArr = ["你", "我", "他", "她", "它", "文", "明", "从", "做", "起", "海", "淘", "测试", "评论"]
    i = 0
    text = ""
    while i < str_len:
        i += 1
        num = randrange(0, len(contentArr))
        text += contentArr[num]
    return text