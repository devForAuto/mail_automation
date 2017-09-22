# -*- coding: utf-8 -*-
"""

@file: base_login_code.py

@time: 2017/8/22 18:07

@desc:

"""
import pymysql
import pymysql.cursors


def getSmsCode(account):
    connection = pymysql.connect(user="csmail_dev", db="csmail_dev",
                                 passwd="oXu1klHx", host="192.168.100.126", port=40000,
                                 cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    sql = "SELECT code FROM login_smscode WHERE phone= '%s'" % (account)
    cur.execute(sql)
    codes = cur.fetchone()
    if codes is None:
        return_code = 325687
    else:
        return_code = codes['code']

    return return_code
