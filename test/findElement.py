# -*- coding: utf-8 -*-
"""

@file: findElement.py.py

@time: 2017/8/24 17:51

@desc:

"""

import unittest
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_case.models import base_login_code
from test_case.models.base_driver import browser


class Tatic(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.base_url = 'http://192.168.100.32:10101/mail/login.html'
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_one(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('account').send_keys('18039271234')
        self.driver.find_element_by_id('passWord').send_keys('test123%pwd')
        self.driver.find_element_by_id('btnSendCode').click()
        sleep(1)
        self.driver.find_element_by_id('smsCode').send_keys(base_login_code.getSmsCode('18039271234'))
        self.driver.find_element_by_id('J_login').click()
        sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='treeDemo_19_span']").click()
        sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='treeDemo_20_span']").click()
        self.driver.switch_to.frame("J_busi_iframe")
        # sleep(2)
        self.driver.find_element_by_link_text("新增母版").click()
        self.driver.find_element(By.ID, "obj_name").send_keys("3622")
        self.driver.find_element(By.LINK_TEXT, "下一步").click()
        sleep(10)
        print(self.driver.page_source)
        # self.driver.find_element(By.ID, "fileField").send_keys("C:\\Users\\QK\\Desktop\母版\\pc-20170818.html")
        # self.driver.switch_to_default_content()
        # self.driver.find_element_by_xpath(".//*[@id='treeDemo_6_span']").click()
        # self.driver.switch_to.frame('J_busi_iframe')
        # sleep(1)
        # self.driver.find_element_by_link_text(u'添加分包策略').click()
        # sleep(3)
        # self.driver.find_element_by_xpath(".//*[@id='tijiao']").click()
        # self.driver.switch_to_default_content()
        # conn = self.driver.find_element_by_xpath(".//*[@id='content:D_msg2']").text
        # self.driver.find_element_by_xpath(".//*[@id='treeDemo_26_span']").click()
        # sleep(2)
        # self.driver.find_element_by_xpath(".//*[@id='treeDemo_33_span']").click()
        # self.driver.switch_to.frame('J_busi_iframe')
        # sleep(3)
        # # self.driver.find_element(By.NAME, "business_name").send_keys("电子发票业务名称测试")
        # # self.driver.find_element(By.CSS_SELECTOR, ".searchBtn").click()
        # # sleep(3)
        # # listreus = self.driver.find_element(By.XPATH, "//*[@id='J_tabletpl']/tr[*]/td[2]")
        # # print(listreus)
        #
        # # current_window = self.driver.current_window_handle
        # # print(self.driver.title)
        # self.driver.find_element(By.LINK_TEXT, u'新增业务').click()
        # self.driver.switch_to_default_content()
        # self.driver.find_element_by_id('busi_type_add').send_keys("电子发票业务名称测试")
        # Select(self.driver.find_element(By.XPATH,".//*[@id='busi_order']")).select_by_value(str(random.randint(1, 5)))
        # sleep(10)
        # self.driver.find_element_by_css_selector(".ui-dialog-autofocus").click()
        # # self.driver.switch_to_default_content()
        # print(self.driver.find_element_by_xpath(".//*[@id='content:D_msg2']").text)
        # all_windows = self.driver.window_handles
        # for window in all_windows:
        #     if window != current_window:
        #         print("here")
        #         self.driver.switch_to.window(window)
        # sleep(3)
        # print(self.driver.current_window_handle)

        # sleep(5)
        # print(self.driver.page_source)
        # self.driver.find_element_by_xpath('/html/body/div[7]/')
        #
        # self.driver.find_element_by_id("busi_type_add").clear()
        # self.driver.find_element(By.ID, "busi_type_add").send_keys("3s")
        # js = "document.getElementById('busi_type_add').click()"
        # self.driver.execute_script(js)

        # sleep(2)
        # businameloc = (By.CSS_SELECTOR, ".searchBtn")
        # self.find_element(businameloc).click()
        # lsloc = (By.XPATH, ".//*[@id='J_tabletpl']/tr[*]/td[2]")
        # sleep(1)
        # listElement = self.find_elements(lsloc)

        # print(listElement)
        # # self.search(listElement)
        sleep(10)
        # self.driver.switch_to.frame("J_busi_iframe")
        # sleep(2)
        # self.driver.find_element(By.LINK_TEXT, "新增母版").click()
        # sleep(1)
        # self.driver.find_element_by_id("templetName").clear()
        # sleep(1)
        # self.driver.find_element_by_id("templetName").send_keys("自动化测试的")
        # Select(self.driver.find_element(By.ID, "templetBusinessType")).select_by_value("F_DZPZ")
        # sleep(0.5)
        # Select(self.driver.find_element(By.ID, "templetBusinessChildType")).select_by_value("S_C_DZPZ_03")
        # self.driver.find_element_by_id("templetMailTopic").clear()
        # self.driver.find_element_by_id("templetMailTopic").send_keys("自动化测试的")
        # Select(self.driver.find_element(By.ID, "templetPostEmail")).select_by_value("10086@139.com")
        # self.driver.find_element_by_css_selector(".normalBtn.BGblue.largeBtn").click()
        # self.driver.switch_to_default_content()
        # sleep(5)
        # self.driver.find_element_by_css_selector(".ui-dialog-autofocus").click()
        # self.driver.find_element_by_id("maskName").send_keys("12")
        # print("下一步查询按钮")
        # self.driver.find_element_by_css_selector(".searchBtn").click()
        # sleep(5)
        # print("下一步确定按钮")
        # self.driver.find_element_by_xpath(".//*[@id='0']/div[3]/a[1]").click()
        # sleep(2)
        # class_loc = self.driver.find_element_by_css_selector(".cke_wysiwyg_frame.cke_reset")
        # self.driver.switch_to.frame(class_loc)
        # self.driver.find_element_by_css_selector(
        #     ".cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders").send_keys("999")
        # sleep(10)
        # self.driver.switch_to.parent_frame()
        # print("下一步提交按钮")
        # var = self.driver.find_element_by_xpath(".//*[@id='J_form_activity']/div[3]/div[3]/a[2]").text
        # print(var)
        # self.driver.find_element_by_xpath(".//*[@id='J_form_activity']/div[3]/div[3]/a[2]").click()
        # sleep(2)
        # print("下一步进入h5母版选择页面")
        # class1_loc = self.driver.find_element_by_css_selector(".cke_wysiwyg_frame.cke_reset")
        # self.driver.switch_to.frame(class1_loc)
        # self.driver.find_element_by_css_selector(
        #     ".cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders").send_keys("999")
        # self.driver.switch_to.parent_frame()
        # sleep(5)
        # a = self.driver.find_element_by_xpath(".//*[@id='J_form_activity']/div[2]/div[3]/a[2]")
        # print(a.text)
        # # ActionChains(self.driver).click(a).perform()
        # # self.driver.find_element_by_link_text(u"保存").click()
        # self.driver.execute_script("$(arguments[0]).click()",a)


    #
    # def find_element(self, loc):
    #     try:
    #         WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(loc).is_displayed())
    #         return self.driver.find_element(loc)
    #     except:
    #         print(u"%s 页面中未能找到 %s 元素" % (self, loc))
    #
    # def find_elements(self, loc):
    #     try:
    #         WebDriverWait(self.driver, 10).until(lambda driver: driver.find_elements(loc).is_displayed())
    #         return self.driver.find_elements(loc)
    #     except:
    #         print(u"%s 页面中未能找到 %s 元素" % (self, loc))
    #
    # def search(self, listss):
    #     ret = []
    #     for i in range(len(listss)):
    #         # print(i)
    #         num = i + 1
    #         var = self.driver.find_element_by_xpath(".//*[@id='J_tabletpl']/tr[%d]/td[2]" % num).text
    #         ret.append(var)
    #     return ret

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
