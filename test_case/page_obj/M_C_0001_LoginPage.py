# -*- coding: utf-8 -*-
"""

@file: LoginPage.py

@time: 2017/8/22 15:32

@desc:

"""
import sys
from selenium.webdriver.common.by import By
from test_case.page_obj.base_obj import Page
from time import sleep
# sys.path.append("..models")
from test_case.models import base_login_code


class login(Page):
    login_username_loc = (By.ID, 'account')
    login_password_loc = (By.ID, 'passWord')
    login_sms_loc = (By.ID, 'smsCode')
    login_sms_button_loc = (By.ID, 'btnSendCode')
    login_button_loc = (By.ID, 'J_login')
    user_login_success_loc = (By.XPATH, ".//*[@id='J_cUserInfo']")

    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_sms_button(self):
        self.find_element(*self.login_sms_button_loc).click()

    def login_sms(self, sms):
        self.find_element(*self.login_sms_loc).send_keys(sms)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def home_login(self, username="username", password="1234567"):
        url = '/mail/login.html'
        self.open(url)
        self.login_username(username)
        self.login_password(password)
        self.login_sms_button()
        sleep(1)
        code = base_login_code.getSmsCode('18039271234')
        self.login_sms(code)
        self.login_button()
        sleep(2)

    def current_url(self):
        return self.get_current_url()

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
