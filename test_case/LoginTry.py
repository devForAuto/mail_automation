# -*- coding: utf-8 -*-
"""

@file: LoginTry.py

@time: 2017/9/14 17:06

@desc:

"""
from time import sleep

from selenium.webdriver.common.by import By
from test_case.A_PublicLogin import is_login


class FindTree():
    def __init__(self):
        self.driver = is_login()

    def test_find_tree(self):
        self.driver.find_element(By.ID, 'treeDemo_4_span').click()
        sleep(10)
if __name__ == "__main__":
    FindTree().test_find_tree()
