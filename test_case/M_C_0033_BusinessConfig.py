# -*- coding: utf-8 -*-
"""

@file: M_C_0033_BusinessConfig.py

@time: 2017/9/15 15:07

@desc: 业务配置

"""
import unittest
from test_case.A_PublicLogin import is_login
from test_case.page_obj.Page_0033_BusinessConfig import MailBusinessConfig
from util import randomUtil


class BusinessConfig(unittest.TestCase):
    dr = is_login()
    flag = False
    BUSICODE = randomUtil.getRandomStrIntLineChine(10)

    def setUp(self, driver=dr):
        self.driver = driver
        self.home = MailBusinessConfig(self.driver)

    def test_0001_busi_cfg_home(self):
        """业务配置主页面"""
        self.home.busi_cfg_home()

    def test_0002_busi_cfg_search(self):
        """业务配置查询"""
        self.home.busi_cfg_add(name=self.BUSICODE, code=randomUtil.getRandomInt(5))
        self.driver.refresh()
        self.home.busi_cfg_search(self.BUSICODE)

    # def test_0003_busi_cfg_add(self):
    #     """业务配置添加"""
    #     self.home.busi_cfg_add(name=randomUtil.getRandomUpperStr(50), code=randomUtil.getRandomInt(20))
    #
    # def test_0004_busi_cfg_add_child(self):
    #     """业务配置添加子业务"""
    #     self.home.busi_cfg_add_child(name=randomUtil.getRandomStr(5),keys=randomUtil.getRandomInt(5))
    def test_z_logout(self):
        """退出"""
        print("退出成功")
        self.flag = True

    def tearDown(self):
        # print(self.flag)
        if self.flag:
            self.driver.quit()
        else:
            self.driver.refresh()


if __name__ == "__main__":
    unittest.main()
