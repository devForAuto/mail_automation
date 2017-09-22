# -*- coding: utf-8 -*-
"""

@file: base_unit.py

@time: 2017/8/22 15:09

@desc:

"""
import unittest
from test_case.models.base_driver import browser


class MyUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        print(u"本测试用执行完毕！")
        # self.driver.quit()
