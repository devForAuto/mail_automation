# -*- coding: utf-8 -*-
"""

@file: Page_0021_MailTemplate.py

@time: 2017/9/11 15:58

@desc: 模板页面

"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base_obj import Page


class MailTemplatePage(Page):
    # 左侧菜单定位
    mail_config_node_tree_loc = (By.XPATH, ".//*[@id='treeDemo_19_span']")
    template_page_node_tree_loc = (By.XPATH, ".//*[@id='treeDemo_21_span']")
    template_page_frame_loc = "J_busi_iframe"
    # 模板添加
    template_page_add_loc = (By.LINK_TEXT, "新增模版")
    template_page_add_templateName_loc = (By.ID, "templetName")
    template_page_add_type_loc = (By.ID, "templetBusinessType")
    template_page_add_child_type_loc = (By.ID, "templetBusinessChildType")
    template_page_add_topicName_loc = (By.ID, "templetMailTopic")
    template_page_add_postEmail_loc = (By.ID, "templetPostEmail")
    template_page_add_next_loc = (By.CSS_SELECTOR, ".normalBtn.BGblue.largeBtn")
    template_page_add_choice_type_loc = (By.CSS_SELECTOR, ".ui-dialog-autofocus")
    template_page_add_pc_search_maskName_loc = (By.ID, "maskName")
    template_page_add_pc_search_searchBtn_loc = (By.CSS_SELECTOR, ".searchBtn")
    template_page_add_pc_search_okBtn_loc = (By.XPATH, ".//*[@id='0']/div[3]/a[1]")
    template_page_add_pc_search_cancel_loc = (By.XPATH, ".//*[@id='0']/div[3]/a[2]")
    template_page_add_pc_edit_frame_class_loc = (By.CSS_SELECTOR, ".cke_wysiwyg_frame.cke_reset")
    template_page_add_pc_edit_frame_loc = ""
    template_page_add_pc_edit_loc = (
        By.CSS_SELECTOR, ".cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders")
    template_page_add_pc_next_loc = (By.XPATH, ".//*[@id='J_form_activity']/div[3]/div[3]/a[2]")
    template_page_add_h5_edit_frame_class_loc = (By.CSS_SELECTOR, ".cke_wysiwyg_frame.cke_reset")
    template_page_add_h5_edit_frame_loc = ""
    template_page_add_h5_edit_loc = (
        By.CSS_SELECTOR, ".cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders")
    template_page_add_h5_save_loc = (By.XPATH, ".//*[@id='J_form_activity']/div[2]/div[3]/a[2]")

    def template_page_home(self):
        """模板配置主页面"""
        self.find_element(*self.mail_config_node_tree_loc).click()
        sleep(1)
        self.find_element(*self.template_page_node_tree_loc).click()

    def template_page_add(self):
        """新增模板"""
        # self.find_element(*self.mail_config_node_tree_loc)
        # self.find_element(*self.template_page_node_tree_loc)
        self.switch_frame(self.template_page_frame_loc)
        self.find_element(*self.template_page_add_loc).click()
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("自动化测试")
        Select(self.find_element(*self.template_page_add_type_loc)).select_by_value("F_DZPZ")
        Select(self.find_element(*self.template_page_add_child_type_loc)).select_by_value("S_C_DZPZ_03")
        self.find_element(*self.template_page_add_topicName_loc).clear()
        self.find_element(*self.template_page_add_topicName_loc).send_keys("自动化测试主题")
        Select(self.find_element(*self.template_page_add_postEmail_loc)).select_by_value("10086@139.com")
        self.find_element(*self.template_page_add_next_loc).click()
        # 弹窗选择在线或者本地
        self.switch_frame_default()
        self.find_element(*self.template_page_add_choice_type_loc).click()
        # pc模板查询选择母版页面
        self.switch_frame(self.template_page_frame_loc)
        self.find_element(*self.template_page_add_pc_search_maskName_loc).send_keys("12")
        self.find_element(*self.template_page_add_pc_search_searchBtn_loc).click()
        sleep(1)
        self.find_element(*self.template_page_add_pc_search_okBtn_loc).click()
        # pc 模板富文本编辑
        self.template_page_add_pc_edit_frame_loc = self.find_element(*self.template_page_add_pc_edit_frame_class_loc)
        self.switch_frame(self.template_page_add_pc_edit_frame_loc)
        self.find_element(*self.template_page_add_pc_edit_loc).send_keys("自动化测试PC富文本编辑框内容输入")
        self.switch_parent_frame()
        self.find_element(*self.template_page_add_pc_next_loc).click()
        sleep(2)
        # h5 页面
        # h5 模板富文本编辑
        self.template_page_add_h5_edit_frame_loc = self.find_element(*self.template_page_add_h5_edit_frame_class_loc)
        self.switch_frame(self.template_page_add_h5_edit_frame_loc)
        sleep(2)
        self.find_element(*self.template_page_add_h5_edit_loc).send_keys("自动化测试h5富文本编辑框内容输入")
        self.switch_parent_frame()
        print(self.find_element(*self.template_page_add_h5_save_loc).text)
        save_btn = self.find_element(*self.template_page_add_h5_save_loc)
        self.script("$(arguments[0]).click()", save_btn)

    # 页面字段校验提示
    template_page_add_name_error_hint = (By.CSS_SELECTOR, '#templet_name_error')

    def template_add_name_empty(self):
        """为空"""
        sleep(1)
        self.switch_frame_default()
        self.switch_frame(self.template_page_frame_loc)
        self.find_element(*self.template_page_add_loc).click()
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_page_add_name_error_hint).text

    def template_add_name_too_long(self):
        """长度大于25字符"""

        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("abcdefghijklmnopqrstuvwxyz")
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_page_add_name_error_hint).text

    template_page_add_type_error_hint = (By.CSS_SELECTOR, '#templetBusinessType_error')

    def template_add_type_empty(self):
        """业务类型为空"""
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("测试")
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_page_add_type_error_hint).text

    template_page_add_child_type_error_hint = (By.CSS_SELECTOR, '#templetBusinessChildType_error')

    def template_add_child_type_empty(self):
        """子业务类型为空"""
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("测试")
        Select(self.find_element(*self.template_page_add_type_loc)).select_by_value("F_DZPZ")
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_page_add_child_type_error_hint).text

    template_page_add_topicName_hint = (By.CSS_SELECTOR, '#templetMailTopic-error')

    def template_add_topicName_empty(self):
        """邮件主题为空"""
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("测试")
        Select(self.find_element(*self.template_page_add_type_loc)).select_by_value("F_DZPZ")
        Select(self.find_element(*self.template_page_add_child_type_loc)).select_by_value("S_C_DZPZ_03")
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_page_add_topicName_hint).text

    def template_add_topicName_too_long(self):
        """邮件主题超长"""
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("测试")
        Select(self.find_element(*self.template_page_add_type_loc)).select_by_value("F_DZPZ")
        Select(self.find_element(*self.template_page_add_child_type_loc)).select_by_value("S_C_DZPZ_03")
        self.find_element(*self.template_page_add_topicName_loc).clear()
        self.find_element(*self.template_page_add_topicName_loc).send_keys("abcdefghijklmnopqrstuvwxyz")
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_page_add_topicName_hint).text

    template_add_postEmail_empty_hint = (By.CSS_SELECTOR, '#busi_email_error')

    def template_add_postEmail_empty(self):
        """邮件主题为空"""
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("测试")
        Select(self.find_element(*self.template_page_add_type_loc)).select_by_value("F_DZPZ")
        Select(self.find_element(*self.template_page_add_child_type_loc)).select_by_value("S_C_DZPZ_03")
        self.find_element(*self.template_page_add_topicName_loc).clear()
        self.find_element(*self.template_page_add_topicName_loc).send_keys("邮件主题")
        self.find_element(*self.template_page_add_next_loc).click()
        return self.find_element(*self.template_add_postEmail_empty_hint).text

    template_add_pc_empty_error_hint = (By.XPATH, ".//*[@id='content:D_msg2']")

    def template_add_pc_empty(self):
        self.find_element(*self.template_page_add_templateName_loc).clear()
        self.find_element(*self.template_page_add_templateName_loc).send_keys("测试")
        Select(self.find_element(*self.template_page_add_type_loc)).select_by_value("F_DZPZ")
        Select(self.find_element(*self.template_page_add_child_type_loc)).select_by_value("S_C_DZPZ_03")
        self.find_element(*self.template_page_add_topicName_loc).clear()
        self.find_element(*self.template_page_add_topicName_loc).send_keys("邮件主题")
        Select(self.find_element(*self.template_page_add_postEmail_loc)).select_by_value("10086@139.com")
        self.find_element(*self.template_page_add_next_loc).click()
        # 弹窗选择在线或者本地
        self.switch_frame_default()
        self.find_element(*self.template_page_add_choice_type_loc).click()
        # pc模板查询选择母版页面
        self.switch_frame(self.template_page_frame_loc)
        self.find_element(*self.template_page_add_pc_search_maskName_loc).send_keys("12")
        self.find_element(*self.template_page_add_pc_search_cancel_loc).click()
        self.find_element(*self.template_page_add_pc_next_loc).click()
        self.switch_frame_default()
        return self.find_element(*self.template_add_pc_empty_error_hint).text
