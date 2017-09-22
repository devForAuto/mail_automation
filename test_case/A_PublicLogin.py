# -*- coding: utf-8 -*-
"""

@file: A_PublicLogin.py

@time: 2017/9/14 15:04

@desc: 公共登录

"""
from selenium.webdriver.common.by import By

from test_case.models.base_driver import browser
from test_case.page_obj.M_C_0001_LoginPage import login


class PublicLogin(object):
    def __init__(self):
        self.driver = browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def public_login(self):
        po = login(self.driver).home_login('18039271234', 'test123%pwd')
        return self.driver
        # try:
        #     self.assertEqual(current_user, expect_user)
        # except AssertionError as e:
        #     print("===")
        # if current_user == expect_user:
        #     print("login Right")
        #     return self.driver
        # else:
        #     print("login o")


# class assertLogin():
#     def __init__(self):
#         self.driver = PublicLogin().public_login()
#
#     def is_login(self):
#         current_user = self.driver.find_element_by_xpath(".//*[@id='J_cUserInfo']").text
#         expect_user = '当前用户：客服邮箱团队/秦文辉(qinwehui)'
#         if current_user == expect_user:
#             print("login Right")
#             self.driver.refresh()
#             return self.driver
#         else:
#             self.driver.quit()
#             PublicLogin().public_login()


def is_login():
    driver = PublicLogin().public_login()
    var = driver.find_element_by_xpath(".//*[@id='J_cUserInfo']").text
    if var == '当前用户：客服邮箱团队/秦文辉(qinwehui)':
        return driver
    else:
        # driver.quit()
        # s = PublicLogin().public_login()
        # s.find_element(By.ID, 'treeDemo_4_span').click()
        print("login error================================")
if __name__ == "__main__":
    is_login()
