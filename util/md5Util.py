# -*- coding: utf-8 -*-
"""

@file: md5Util.py

@time: 2017/9/27 9:37

@desc:

"""
import hashlib

'''md5 加密'''


def md5(srt):
    m = hashlib.md5()
    m.update(srt.encode("utf-8"))
    return m.hexdigest()
