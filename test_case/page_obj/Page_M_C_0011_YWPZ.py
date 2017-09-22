# -*- coding: utf-8 -*-
"""

@file: Page_M_C_0011_YWPZ.py

@time: 2017/9/4 20:44

@desc:

"""
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_case.page_obj.base_obj import Page
from time import sleep


class BusiType(Page):
    # 左侧菜单元素定位
    busi_b_tree_loc = (By.XPATH, ".//*[@id='treeDemo_26_span']")
    busi_tree_loc = (By.XPATH, ".//*[@id='treeDemo_33_span']")
    # 主页Frame
    busi_tree_frame_loc = 'J_busi_iframe'
    # 页面搜索元素定位
    businame_search_by_name_loc = (By.NAME, "business_name")
    businame_search_btn_loc = (By.CSS_SELECTOR, ".searchBtn")
    busilist_search_result_loc = (By.XPATH, ".//*[@id='J_tabletpl']/tr[*]/td[2]")
    businame_for_assert_loc = (By.XPATH, ".//*[@id='J_tabletpl']/tr%s/td[2]")  # 查询列表中具体字段元素定位
    busilist_search_result_del_loc = (By.XPATH, ".//*[@id='J_tabletpl']/tr%s/td[9]/div/a[4]")
    # 添加页面元素
    busi_add_btm_loc = (By.LINK_TEXT, u'新增业务')
    busi_add_name_loc = (By.XPATH, ".//*[@id='busi_type_add']")
    busi_add_key_loc = (By.XPATH, ".//*[@id='business_key']")
    busi_add_busi_order_loc = (By.XPATH, ".//*[@id='busi_order']")
    busi_add_sub_btn_loc = (By.CSS_SELECTOR, '.ui-dialog-autofocus')
    busi_add_page_hits_loc = (By.XPATH, ".//*[@id='content:D_msg2']")

    # 错误提示信息
    businame_empty_loc = (By.XPATH, ".//*[@id='content:D_msg2']")

    def busi_tree_home(self):
        self.find_element(*self.busi_b_tree_loc).click()
        sleep(1)
        self.find_element(*self.busi_tree_loc).click()
        sleep(1)

    def busicode_add(self, busi_type, busi_key):
        self.switch_frame(self.busi_tree_frame_loc)
        self.find_element(*self.busi_add_btm_loc).click()
        sleep(1)
        self.switch_frame_default()
        self.find_element(*self.busi_add_name_loc).send_keys(busi_type)
        self.find_element(*self.busi_add_key_loc).send_keys(busi_key)
        Select(self.find_element(*self.busi_add_busi_order_loc)).select_by_value(str(random.randint(1, 5)))
        self.find_element(*self.busi_add_sub_btn_loc).click()

    def busicode_exist(self, busi_type):
        self.switch_frame_default()
        self.switch_frame(self.busi_tree_frame_loc)
        self.find_element(*self.busi_add_btm_loc).click()
        self.switch_frame_default()
        self.find_element(*self.busi_add_name_loc).send_keys(busi_type)
        self.find_element(*self.busi_add_sub_btn_loc).click()

    def businame_search(self, busi_name=''):
        self.switch_frame_default()
        self.switch_frame(self.busi_tree_frame_loc)
        self.find_element(*self.businame_search_by_name_loc).clear()
        self.find_element(*self.businame_search_by_name_loc).send_keys(busi_name)
        sleep(1)
        self.find_element(*self.businame_search_btn_loc).click()
        sleep(1)
        list_result = self.find_elements(*self.busilist_search_result_loc)
        search_name = self.search_result(list_result, self.businame_for_assert_loc)
        return search_name

    def businame_empty(self, busi_name=''):
        self.switch_frame_default()
        self.switch_frame(self.busi_tree_frame_loc)
        self.find_element(*self.busi_add_btm_loc).click()
        self.switch_frame_default()
        self.find_element(*self.busi_add_sub_btn_loc).click()
        return self.find_element(*self.businame_empty_loc).text

    def busilist_search_result_del(self):
        self.find_element(*self.busilist_search_result_del_loc).click()
