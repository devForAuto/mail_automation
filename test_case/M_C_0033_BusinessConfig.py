# -*- coding: utf-8 -*-
"""

@file: M_C_0033_BusinessConfig.py

@time: 2017/9/15 15:07

@desc: 业务配置

"""
import unittest
from test_case.A_PublicLogin import is_login
from test_case.page_obj.Page_0033_BusinessConfig import MailBusinessConfig


class BusinessConfig(unittest.TestCase):
    dr = is_login()

    def setUp(self, driver=dr):
        self.driver = driver
        home = MailBusinessConfig(self.driver)

    def test_0001_busi_cfg_home(self):
        MailBusinessConfig(self.driver).busi_cfg_home()

    # def test_0002_busi_cfg_search(self):
    #     MailBusinessConfig(self.driver).busi_cfg_search()

    def test_0003_busi_cfg_add(self):
        """添加页面"""
        MailBusinessConfig(self.driver).busi_cfg_add()

    def test_0004_busi_cfg_add_child(self):
        """添加子业务"""

    def tearDown(self):
        self.driver.refresh()


if __name__ == "__main__":
    unittest.main()
