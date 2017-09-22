# -*- coding: utf-8 -*-
"""

@file: M_C_0002_billFileTatic.py

@time: 2017/8/22 23:38

@desc:

"""
import unittest
from test_case.models.base_driver import browser
from test_case.page_obj.M_C_0001_LoginPage import login

from test_case.page_obj.M_C_0002_billFileTaticPage import billFileTactic


class FilebillFileTactic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_001_home(self):
        '''进入分包策略配置主页面'''

        login(self.driver).home_login('18039271234', 'test123%pwd')
        billFileTactic(self.driver).billFileTactic_home()

    def test_002_search_billFileTactic(self):
        """查询"""
        billFileTactic(self.driver).search_billFileTactic()

    def test_003_add_billFileTactic(self):
        """添加策略包"""
        billFileTactic(self.driver).add_billFileTactic()

    def test_004_error_billFileTactic_province(self):
        """省份编码不输入提示"""
        print(billFileTactic(self.driver).error_billFileTactic_province_loc())
        # self.assertEqual(, u'省份不能为空!')

    def test_z_driver_out(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.refresh()
        except Exception as e:
            print(e)
        finally:
            print("")


if __name__ == "__main__":
    unittest.main()
