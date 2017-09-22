# -*- coding: utf-8 -*-
"""

@file: M_C_0021_MailTemplate.py

@time: 2017/9/12 11:28

@desc:

"""
import unittest

from test_case.models.base_driver import browser
from test_case.page_obj.M_C_0001_LoginPage import login
from test_case.page_obj.Page_0021_MailTemplate import MailTemplatePage


class MailTemplate(unittest.TestCase):
    """邮件配置管理-模板管理"""

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_0001_mail_template_home(self):
        """模板配置配置主页面"""
        login(self.driver).home_login('18039271234', 'test123%pwd')
        MailTemplatePage(self.driver).template_page_home()

    # def test_0002_mail_template_add(self):
    #     """增加模板"""
    #     MailTemplatePage(self.driver).template_page_add()

    def test_0003_mail_template_add_name_empty(self):
        """添加模板名称为空"""
        hint = MailTemplatePage(self.driver).template_add_name_empty()
        print(hint)
        self.assertEqual(hint, '必填项，长度不超过25个字符')

    def test_0004_mail_template_add_name_to_long(self):
        """添加模板名称超长"""
        hint = MailTemplatePage(self.driver).template_add_name_too_long()
        print(hint)
        self.assertEqual(hint, '必填项，长度不超过25个字符')

    def test_0005_mail_template_add_type_empty(self):
        """业务类型为空"""
        hint = MailTemplatePage(self.driver).template_add_type_empty()
        print(hint)
        self.assertEqual(hint, '请选择业务类型')

    def test_0006_mail_template_add_name_child_type_empty(self):
        """子业务为空（有子业务）"""
        hint = MailTemplatePage(self.driver).template_add_child_type_empty()
        print(hint)
        self.assertEqual(hint, '请选择子业务')

    def test_0007_mail_template_add_topicName_empty(self):
        """邮件主题为空"""
        hint = MailTemplatePage(self.driver).template_add_topicName_empty()
        print(hint)
        self.assertEqual(hint, '必填项，长度不超过25个字符')

    def test_0008_mail_template_add_topicName_too_long(self):
        """邮件主题超长"""
        hint = MailTemplatePage(self.driver).template_add_topicName_too_long()
        print(hint)
        self.assertEqual(hint, '必填项，长度不超过25个字符')

    def test_0009_mail_template_add_postEmail_too_long(self):
        """发送邮箱未选择"""
        hint = MailTemplatePage(self.driver).template_add_postEmail_empty()
        print(hint)
        self.assertEqual(hint, '请选择发送邮箱')

    def test_0010_mail_template_add_pc_empty(self):
        """PC模板未选择"""
        hint = MailTemplatePage(self.driver).template_add_pc_empty()
        print(hint)
        self.assertEqual(hint, '请选择母版后，进入下一步')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
