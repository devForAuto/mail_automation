# -*- coding: utf-8 -*-
"""

@file: run_case.py.py

@time: 2017/8/24 9:52

@desc:

"""
import unittest
from HTMLTestRunner import HTMLTestRunner

import time


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = './report/' + now + '_result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='客服邮箱管理系统',
                            description=u'环境：windows 10 浏览器:chrome')
    discover = unittest.defaultTestLoader.discover('./test_case',
                                                   pattern='M_C_0033*.py')
    runner.run(discover)
    fp.close()

