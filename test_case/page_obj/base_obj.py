# -*- coding: utf-8 -*-
"""

@file: base_obj.py

@time: 2017/8/22 15:13

@desc:

"""

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pyapilog import pyapilog

class Page(object):
    bbs_url = 'https://192.168.100.32:10143'
    # bbs_url = 'http://192.168.100.32:10909'

    # bbs_url = 'http://www.baidu.com' https://192.168.100.32:10143/mail/login.html

    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.change_tuple_loc = ''
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        load_url = self.base_url + url
        pyapilog().info("%s 打开URL：%s" % (self, load_url))
        self.driver.get(load_url)
        assert self.on_page(url), 'did not land on %s' + load_url

    def find_element(self, *loc):
        try:
            pyapilog().info("%s 页面定位元素：%s" % (self, loc))
            return self.driver.find_element(*loc)
        except:
            pyapilog().info(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 下拉框
    def select(self, *loc):
        try:
            pyapilog().info("%s 下拉菜单元素：%s" % (self, loc))
            return Select(self.find_element(*loc))
        except:
            pyapilog().info(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def page_source(self):
        return self.driver.page_source

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def switch_frame(self, loc):
        try:
            pyapilog().info("%s 切换frame元素：%s" % (self, loc))
            WebDriverWait(self.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(loc))
            # return self.driver.switch_to.frame(loc)
        except:
            pyapilog().info(u"%s 页面中切换 %s 元素失败！" % (self, loc))

    def switch_parent_frame(self):
        pyapilog().info("%s 切换父级frame！" % self)
        self.driver.switch_to.parent_frame()

    def switch_frame_default(self):
        pyapilog().info("%s 退出frame！" % self)
        self.driver.switch_to.default_content()

    def switch_to_alter(self):
        return self.driver.switch_to_alert()

    def search_result(self, lists, search_loc):
        ret = []
        for i in range(len(lists)):
            num = i + 1

            if len(lists) == 1:
                # 改变元祖的值
                change_tuple_loc = (search_loc[0], search_loc[1] % '')
            else:
                change_tuple_loc = (search_loc[0], search_loc[1] % ('[%d]' % num))
            self.change_tuple_loc = change_tuple_loc
            var = self.find_element(*self.change_tuple_loc).text
            ret.append(var)
        return ret

    def open(self, url):
        self._open(url)

    def on_page(self, url):
        return self.driver.current_url == (self.base_url + url)

    def script(self, src, args):
        pyapilog().info("%s js定位元素：%s" % (self, args))
        return self.driver.execute_script(src, args)

    def get_current_url(self):
        return self.driver.current_url
#