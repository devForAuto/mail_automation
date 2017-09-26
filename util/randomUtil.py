# -*- coding: utf-8 -*-
"""

@file: randomUtil.py

@time: 2017/9/26 14:36

@desc:

"""
import random

# 固定随机数字
def getRandomInt(length):
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    splice = random.sample(code_list, length)
    return int(''.join(splice))

# 固定长度随机大小写字母
def getRandomStr(length):
    code_list = []
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    splice = random.sample(code_list, length)
    return ''.join(splice)

# 固定长度大写字母
def getRandomUpperStr(length):
    code_list = []
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    splice = random.sample(code_list, length)
    return ''.join(splice)


# getRandomStr(5)
for i in range(100):
    print(getRandomStr(9))
    print(getRandomInt(9))
    print(getRandomUpperStr(9))
