# -*- coding: utf-8 -*-
"""

@file: Page_0033_BusinessConfig.py

@time: 2017/9/15 15:19

@desc:

"""
from time import sleep

from selenium.webdriver.common.by import By

from test_case.page_obj.base_obj import Page


class MailBusinessConfig(Page):
    # 左侧菜单元素定位
    mail_config_note_tree_loc = (By.XPATH, ".//*[@id='treeDemo_26_span']")
    busi_cfg_note_tree_loc = (By.XPATH, ".//*[@id='treeDemo_33_span']")
    # frame 定位
    busi_cfg_home_frame_loc = "J_busi_iframe"
    # 搜索元素定位
    busi_cfg_search_name_loc = (By.NAME, 'business_name')
    busi_cfg_search_btn_loc = (By.CSS_SELECTOR, '.searchBtn')

    # 新增页面元素定位
    busi_cfg_add_loc = (By.LINK_TEXT, '新增业务')
    busi_cfg_add_name_loc = (By.ID, 'busi_type_add')
    busi_cfg_add_key = (By.ID, 'business_key')
    busi_cfg_add_okBtn = (By.CSS_SELECTOR, '.ui-dialog-autofocus')
    # 子业务添加定位
    busi_cfg_child_add_loc = (By.LINK_TEXT, '添加子业务')
    busi_cfg_child_name_loc = (By.ID, 'busi_child_name_add')
    busi_cfg_child_key_loc = (By.ID, 'busi_child_key_coding')
    busi_cfg_child_account_loc = (By.ID, 'account1')
    busi_cfg_child_okBtn_loc = (By.CSS_SELECTOR, '.ui-dialog-autofocus:nth-child(1)')

    def busi_cfg_home(self):
        self.find_element(*self.mail_config_note_tree_loc).click()
        sleep(1)
        self.find_element(*self.busi_cfg_note_tree_loc).click()

    def busi_cfg_search(self, sName=''):
        """搜索"""
        self.busi_cfg_home()
        sleep(1)
        self.switch_frame(self.busi_cfg_home_frame_loc)
        self.find_element(*self.busi_cfg_search_name_loc).send_keys(sName)
        sleep(3)
        self.find_element(*self.busi_cfg_search_btn_loc).click()

    def busi_cfg_add(self, name='ywbm', code='1256'):
        """添加业务配置"""
        self.busi_cfg_home()
        self.switch_frame(self.busi_cfg_home_frame_loc)
        self.find_element(*self.busi_cfg_add_loc).click()
        self.switch_frame_default()
        self.find_element(*self.busi_cfg_add_name_loc).clear()
        self.find_element(*self.busi_cfg_add_name_loc).send_keys(name)
        self.find_element(*self.busi_cfg_add_key).clear()
        self.find_element(*self.busi_cfg_add_key).send_keys(code)
        sleep(10)
        self.find_element(*self.busi_cfg_add_okBtn).click()

    def busi_cfg_add_child(self, name='', keys=''):
        """子业务"""
        # self.busi_cfg_home()
        # self.switch_frame(self.busi_cfg_home_frame_loc)
        self.busi_cfg_search(sName='AaCE')
        # self.find_element(*self.busi_cfg_search_name_loc).send_keys('AaCE')
        # self.find_element(*self.busi_cfg_search_btn_loc).click()
        # sleep(3)
        self.find_element(*self.busi_cfg_child_add_loc).click()
        sleep(3)
        self.switch_frame_default()
        self.find_element(*self.busi_cfg_child_name_loc).clear()
        self.find_element(*self.busi_cfg_child_name_loc).send_keys(name)
        self.find_element(*self.busi_cfg_child_key_loc).clear()
        self.find_element(*self.busi_cfg_child_key_loc).send_keys(keys)
        # self.select(*self.busi_cfg_child_account_loc).select_by_value("A1001")
        self.select(*self.busi_cfg_child_account_loc).select_by_index(2)
        sleep(2)
        self.find_element(*self.busi_cfg_child_okBtn_loc).click()
        sleep(10)
