# -*- coding: utf-8 -*-
"""

@file: billFileTacticPage.py

@time: 2017/8/22 20:32

@desc:

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base_obj import Page
from time import sleep
import random


class billFileTactic(Page):
    billFileTactic_loc = (By.XPATH, ".//*[@id='treeDemo_6_span']")
    billFileTactic_frame_loc = 'J_busi_iframe'
    billFileTactic_search_by_tacticName_loc = (By.ID, 'tacticName')
    billFileTactic_search_submit_loc = (By.CLASS_NAME, 'searchBtn')
    add_billFileTactic_loc = (By.LINK_TEXT, '添加分包策略')

    #  u策略包添加
    add_billFileTactic_province_loc = (By.ID, 'provinceCode1')
    add_billFileTactic_tacticName_loc = (By.ID, 'tacticName')
    add_billFileTactic_billType_loc = (By.ID, 'type')
    add_billFileTactic_tacticType_loc = (By.ID, 'tacticType')
    add_billFileTactic_isResolve_loc = (By.ID, 'isResolve')
    add_billFileTactic_filePath_loc = (By.ID, 'filePath')
    add_billFileTactic_fileName_loc = (By.ID, 'fileName')
    add_billFileTactic_passwd_loc = (By.ID, 'passwd')
    add_billFileTactic_weight_loc = (By.ID, 'weight')
    add_billFileTactic_submit_loc = (By.XPATH, ".//*[@id='tijiao']")
    add_error_billFileTactic_province_loc = (By.XPATH, ".//*[@id='content:D_msg2']")

    def billFileTactic_home(self):
        u"""进入文件分包管理主页面"""
        self.find_element(*self.billFileTactic_loc).click()
        self.switch_frame(self.billFileTactic_frame_loc)

    def search_billFileTactic(self):
        u"""查询策略名称"""
        self.find_element(*self.billFileTactic_search_by_tacticName_loc).send_keys('ttttttttttt')
        self.find_element(*self.billFileTactic_search_submit_loc).click()
        print("------------------------search_billFileTactic--------------------------------------------")
        self.switch_frame_default()

    def add_billFileTactic(self):
        """添加文件分包策略"""
        #  u添加页面
        self.switch_frame(self.billFileTactic_frame_loc)
        self.find_element(*self.add_billFileTactic_loc).click()
        Select(self.find_element(*self.add_billFileTactic_province_loc)).select_by_value('bj')
        name = u"北京全量分包" + str(random.randint(1, 100))
        print(name)
        self.find_element(*self.add_billFileTactic_tacticName_loc).send_keys(name)
        Select(self.find_element(*self.add_billFileTactic_billType_loc)).select_by_value('hfzd')
        Select(self.find_element(*self.add_billFileTactic_tacticType_loc)).select_by_value('1')
        Select(self.find_element(*self.add_billFileTactic_isResolve_loc)).select_by_value('1')
        self.find_element(*self.add_billFileTactic_filePath_loc).send_keys("/upload/")
        self.find_element(*self.add_billFileTactic_fileName_loc).send_keys(".*gz")
        self.find_element(*self.add_billFileTactic_passwd_loc).send_keys("bill")
        self.find_element(*self.add_billFileTactic_weight_loc).send_keys(random.randint(1, 100))
        self.find_element(*self.add_billFileTactic_submit_loc).click()
        sleep(2)
        self.switch_frame_default()

    def error_billFileTactic_province_loc(self):
        u"""省份编码不选择，提示"""
        self.switch_frame(self.billFileTactic_frame_loc)
        self.find_element(*self.add_billFileTactic_loc).click()
        self.find_element(*self.add_billFileTactic_submit_loc).click()
        sleep(1)
        self.switch_frame_default()
        return self.find_element(*self.add_error_billFileTactic_province_loc).text
