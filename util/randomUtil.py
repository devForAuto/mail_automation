# -*- coding: utf-8 -*-
"""

@file: randomUtil.py

@time: 2017/9/26 14:36

@desc:

"""
import random
import math, string


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


# 字母数字组合下划线汉字
def getRandomStrIntLineChine(length):
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    for i in range(0x4E00, 0x9FA5):
        code_list.append(chr(i))
    code_list.append(chr(95))
    splice = random.sample(code_list, length)
    return ''.join(splice)


# 字母数字组合下划线
def getRandomStrIntLine(length):
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    code_list.append(chr(95))
    splice = random.sample(code_list, length)
    return ''.join(splice)


# 字母数字组合
def getRandomStrInt(length):
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    splice = random.sample(code_list, length)
    return ''.join(splice)


# 汉字
def Unicode(length):
    code_list = []
    # val = random.randint(0x4E00, 0x9FA5)
    for i in range(0x4E00, 0x9FA5):
        code_list.append(chr(i))
    splice = random.sample(code_list, length)
    return ''.join(splice)

# for i in range(1000):
#     # print(getRandomStr(9))
#     # print(getRandomStrIntLine(9))
#     # print(getRandomUpperStr(9))
#     print(Unicode(10))
