# -*- coding: utf-8 -*-
"""

@file: uuidUtil.py

@time: 2017/9/27 9:38

@desc:

"""
import uuid


def getUUID():
    uid = str(uuid.uuid4())
    print(len(uid.replace('-', '')))
    return uid.replace('-', '')


print(getUUID())
