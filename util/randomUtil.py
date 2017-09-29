# -*- coding: utf-8 -*-
"""

@file: randomUtil.py

@time: 2017/9/26 14:36

@desc:

"""
import random

_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
_uppChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
_lowChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
_allChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '1',
             '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']


# 固定随机数字
def getRandomInt(length):
    chars = '1234567890'
    num = ''
    rd = random.Random()
    for j in range(length):
        num += chars[rd.randint(0, len(chars) - 1)]
    return num


# 固定长度随机大小写字母
def getRandomStr(length):
    chars = []
    for i in range(length):
        chars.append(random.choice(_uppChars + _lowChars))
    return ''.join(chars)


# 固定长度大写字母
def getRandomUpperStr(length):
    chars = []
    for i in range(length):
        chars.append(random.choice(_uppChars))
    return ''.join(chars)


# 固定长度小写字母
def getRandomLowerStr(length):
    return getRandomUpperStr(length).lower()


# 大写字母数字
def getRandomUpperInt(length):
    chars = []
    for i in range(length - 1):
        chars.append(random.choice(_uppChars + _nums))
    chars.append(str(random.randint(0, 9)))
    # print(chars)
    random.shuffle(chars)
    return ''.join(chars)


# 字母数字组合下划线汉字
def getRandomStrIntLineChine(length):
    code_list = []
    chine_list = []
    str_list = []
    for i in range(10):  # 0-9数字
        str_list.append(str(i))
    for i in range(65, 91):  # A-Z
        str_list.append(chr(i))
    for i in range(97, 123):  # a-z
        str_list.append(chr(i))
    for i in range(0x4E00, 0x9FA5):
        chine_list.append(chr(i))
    if length >= 2:
        splice_chine = random.sample(chine_list, 2)
        splice_str = random.sample(str_list, length - 2)
    code_list.append(chr(95))
    code_list = code_list + splice_str + splice_chine
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
    for i in range(length - 1):
        code_list.append(random.choice(_nums + _uppChars + _lowChars))
    code_list.append(str(random.randint(0, 9)))
    random.shuffle(code_list)
    return ''.join(code_list)


    # splice = random.sample(splice, length)
    # return ''.join(splice)


# 汉字
def getRandomChine(length):
    code_list = []
    # val = random.randint(0x4E00, 0x9FA5)
    for i in range(0x4E00, 0x9FA5):
        code_list.append(chr(i))
    splice = random.sample(code_list, length)
    return ''.join(splice)
#
#
# for i in range(100):
#     #     # print(getRandomStr(9))
#     #     # print(getRandomStrIntLine(9))
#     print(getRandomLowerStr(8))
#
# # print(Unicode(10))
