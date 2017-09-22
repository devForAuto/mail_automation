# -*- coding: utf-8 -*-
"""

@file: login_case.py.py

@time: 2017/8/22 16:00

@desc:

"""
import unittest

from test_case.models.base_driver import browser
from test_case.page_obj.M_C_0001_LoginPage import login
from test_case.page_obj.M_C_0002_billFileTaticPage import billFileTactic


class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def user_login_verify(self, username='', password=''):
        login(self.driver).home_login(username, password)

    def test_login(self):
        self.user_login_verify(username='18039271234', password='test123%pwd')
        po = login(self.driver)
        # self.assertEqual(po.user_login_success(), '')
        print(po.current_url())
        print(po.user_login_success())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
