# -*- coding: utf-8 -*-
"""

@file: M_C_0011_YWPZ.py

@time: 2017/9/4 20:39

@desc: 业务配置

"""
import unittest
from test_case.models.base_driver import browser
from test_case.page_obj.Page_M_C_0011_YWPZ import BusiType
from test_case.page_obj.M_C_0001_LoginPage import login


class Ywpz(unittest.TestCase):
    BUSI_NAME = '电子发票业务名称测试'
    BUSI_KEY = 'DZFP_YW_001'

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_01_into_ywbm_home(self):
        '''进入页面编码主页面'''
        login(self.driver).home_login('18039271234', 'test123%pwd')
        BusiType(self.driver).busi_tree_home()

    def test_02_add_ywbm(self):
        '''添加业务编码'''
        # 判断添加的业务编码是存在，存在则删除
        # search_result = BusiType(self.driver).businame_search(busi_name=self.BUSI_NAME)
        # if self.BUSI_NAME in search_result:
        #     # 删除
        #     print("====================")
        # else:
        #     print("-=-=-=-==---=-=-=-=-")
        BusiType(self.driver).busicode_add(self.BUSI_NAME, self.BUSI_KEY)
        search_result = BusiType(self.driver).businame_search(busi_name=self.BUSI_NAME)
        self.assertEqual(search_result[0], self.BUSI_NAME)
        print(search_result[0])

    def test_03_search_ywbm(self):
        '''查询页面页面编码'''
        search_result = BusiType(self.driver).businame_search(busi_name='')
        print("查询结果：")
        if len(search_result) == 0:
            print(len(search_result))
        else:
            print(search_result)

    def test_04_businame_is_empty(self):
        '''业务编码为空'''
        search_result = BusiType(self.driver).businame_empty(busi_name='')
        print(search_result)

    @classmethod
    def tearDownClass(cls):
        try:
            # cls.driver.refresh()
            cls.driver.quit()
        except Exception as e:
            print(e)
        finally:
            print("")


if __name__ == "__main__":
    unittest.main()
