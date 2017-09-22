# -*- coding: utf-8 -*-
"""

@file: Page_0020_MasterPage.py

@time: 2017/9/11 15:17

@desc: 母版页面

"""
from time import sleep

from selenium.webdriver.common.by import By

from test_case.page_obj.base_obj import Page


class MasterPage(Page):
    # 左侧菜单定位
    mail_config_node_tree_loc = (By.XPATH, ".//*[@id='treeDemo_19_span']")
    master_page_node_tree_loc = (By.XPATH, ".//*[@id='treeDemo_20_span']")
    master_page_frame_loc = "J_busi_iframe"
    master_add_loc = (By.LINK_TEXT, "新增母版")
    # 母版添加元素定位
    master_add_name_loc = (By.ID, "obj_name")  # 母版名称
    master_add_next_loc = (By.LINK_TEXT, "下一步")  # PC下一步
    master_add_pc_file_loc = (By.ID, "fileField")  # PC模板上传按钮
    master_add_pc_next_loc = (By.LINK_TEXT, u"下一步")  # PC下一步
    master_add_h5_file_loc = (By.ID, "fileField")  # H5模板上传按钮
    master_add_h5_save_loc = (By.LINK_TEXT, "保存")  # H5 保存按钮
    file_a_abc_loc = (By.ID, "fileField")
    # 母版审核
    master_search_name_loc = (By.ID, "obj_name")
    master_search_btn_loc = (By.LINK_TEXT, "查询")
    master_review_btn_loc = (By.LINK_TEXT, "审核")
    master_review_page_pass_loc = (By.LINK_TEXT, "审核通过")

    def master_page_home(self):
        """母版配置主页面"""
        self.find_element(*self.mail_config_node_tree_loc).click()
        sleep(1)
        self.find_element(*self.master_page_node_tree_loc).click()

    def master_page_add(self):
        """新增母版"""
        self.switch_frame(self.master_page_frame_loc)
        self.find_element(*self.master_add_loc).click()
        self.find_element(*self.master_add_name_loc).send_keys("母版添加自动化测试")
        self.find_element(*self.master_add_next_loc).click()
        # 选择PC母版上传
        sleep(1)
        self.find_element(*self.master_add_pc_file_loc).send_keys('C:/Users/QK/Desktop/mu/pc-20170818.html')
        sleep(1)
        self.find_element(*self.master_add_pc_next_loc).click()
        sleep(1)
        # 选择h5母版上传
        self.find_element(*self.master_add_h5_file_loc).send_keys("C:/Users/QK/Desktop/mu/h5-20170818.html")
        sleep(1)
        print("H5已上传，待提交")
        save_btn = self.find_element(*self.master_add_h5_save_loc)
        sleep(1)
        self.script("$(arguments[0]).click()", save_btn)
        self.switch_frame_default()

    def master_page_review(self):
        """母版审核"""
        self.switch_frame(self.master_page_frame_loc)
        self.find_element(*self.master_search_name_loc).send_keys("母版添加自动化测试")
        self.find_element(*self.master_search_btn_loc).click()
        self.find_element(*self.master_review_btn_loc).click()
        self.find_element(*self.master_review_page_pass_loc).click()
        sleep(5)
