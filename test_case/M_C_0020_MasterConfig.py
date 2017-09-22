# -*- coding: utf-8 -*-
"""

@file: M_C_0020_MasterConfig.py

@time: 2017/9/12 16:42

@desc: 母版配置

"""
import unittest

from test_case.models.base_driver import browser
from test_case.page_obj.M_C_0001_LoginPage import login
from test_case.page_obj.Page_0020_MasterPage import MasterPage


class MasterConfig(unittest.TestCase):
    """邮件配置管理-母板管理"""
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_0001_master_home(self):
        """母版配置主页面"""
        login(self.driver).home_login('18039271234', 'test123%pwd')
        MasterPage(self.driver).master_page_home()

    def test_0002_master_add(self):
        """添加母版"""
        MasterPage(self.driver).master_page_add()

    def test_0003_master_review(self):
        """母版审核"""
        MasterPage(self.driver).master_page_review()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
