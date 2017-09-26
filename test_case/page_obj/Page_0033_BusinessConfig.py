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

    def busi_cfg_home(self):
        self.find_element(*self.mail_config_note_tree_loc).click()
        sleep(1)
        self.find_element(*self.busi_cfg_note_tree_loc).click()

    def busi_cfg_search(self, sName=''):
        self.find_element(*self.mail_config_note_tree_loc).click()
        sleep(1)
        self.find_element(*self.busi_cfg_note_tree_loc).click()
        sleep(1)
        self.switch_frame(self.busi_cfg_home_frame_loc)
        self.find_element(*self.busi_cfg_search_name_loc).send_keys(sName)
        sleep(3)
        self.find_element(*self.busi_cfg_search_btn_loc).click()

    def busi_cfg_add(self, name='ywbm', code='1256'):
        self.busi_cfg_home()
        self.switch_frame(self.busi_cfg_home_frame_loc)
        self.find_element(*self.busi_cfg_add_loc).click()
        self.switch_frame_default()
        self.find_element(*self.busi_cfg_add_name_loc).clear()
        self.find_element(*self.busi_cfg_add_name_loc).send_keys(name)
        self.find_element(*self.busi_cfg_add_key).clear()
        self.find_element(*self.busi_cfg_add_key).send_keys(code)
        sleep(2)
        self.find_element(*self.busi_cfg_add_okBtn).click()

    def busi_cfg_add_child(self):
        """子业务"""
