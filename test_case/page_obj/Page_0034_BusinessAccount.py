#-*-coding:utf-8-*-

from test_case.page_obj.base_obj import Page
from selenium.webdriver.common.by import By
from time import sleep


class MailBusinessAccount(Page):
    #左侧菜单元素定位：系统管理-业务帐号管理
    mail_system_note_tree_loc = (By.XPATH, ".//*[@id='treeDemo_26_span']")
    account_cfg_note_tree_loc = (By.XPATH, ".//*[@id='treeDemo_34_span']")

    #添加帐号页面元素定位
    account_cfg_add_loc = (By.ID,"addAccountBtn")  #添加帐号
    account_cfg_add_level_loc = (By.ID,"account_level")  #优先级
    account_cfg_add_account_loc = (By.ID,"account") #帐号
    account_cfg_add_pass_loc = (By.ID,'pass') #密码
    account_cfg_add_confirmpass_loc = (By.ID,"confirm_pass") #确认密码
    account_cfg_add_okbtn_loc = (By.XPATH,"html/body/div[7]/div/table/tbody/tr[3]/td/div[2]/button[1]") #提交按钮
    account_cfg_add_okbtn_assert=(By.XPATH, ".//*[@id='content:D_msg2']")  #提示信息


    #搜索页面定位
    account_cfg_search_account_loc = (By.ID, "account")  # 帐号
    account_cfg_search_state_loc = (By.NAME, "state") #状态
    account_cfg_search_level_loc = (By.NAME, "account_level") #优先级
    account_cfg_search_button_loc = (By.ID, "searchBtn") #搜索
    account_cfg_search_assert_loc = (By.XPATH,".//*[@id='J_tabletpl']/tr[1]/td[1]")


    #frame定位
    account_cfg_home_frame_loc ="J_busi_iframe"

    def account_cfg_home(self):
        self.find_element(*self.mail_system_note_tree_loc).click()
        sleep(1)
        self.find_element(*self.account_cfg_note_tree_loc).click()
        self.switch_frame(self.account_cfg_home_frame_loc)

    def account_cfg_add(self,level="1",account="A0014",passa="A123a123",confirmPass="A123a123"):
        """添加帐号"""
        self.account_cfg_home()

        self.find_element(*self.account_cfg_add_loc).click()
        self.switch_frame_default()

        self.select(*self.account_cfg_add_level_loc).select_by_value(level)

        self.find_element(*self.account_cfg_add_account_loc).clear()
        self.find_element(*self.account_cfg_add_account_loc).send_keys(account)

        self.find_element(*self.account_cfg_add_pass_loc).clear()
        self.find_element(*self.account_cfg_add_pass_loc).send_keys(passa)

        self.find_element(*self.account_cfg_add_confirmpass_loc).clear()
        self.find_element(*self.account_cfg_add_confirmpass_loc).send_keys(confirmPass)

        sleep(1)
        self.find_element(*self.account_cfg_add_okbtn_loc).click()
        sleep(1)

        # 校验添加帐号、搜索帐号结果
        self.switch_frame(self.account_cfg_home_frame_loc)
        sleep(5)
        return self.find_element(*self.account_cfg_search_assert_loc).text

    def account_cfg_search(self, account="",state="全部",level="全部"):
        """帐号搜索"""
        self.account_cfg_home()
        #self.switch_frame(self.account_cfg_home_frame_loc)

        self.find_element(*self.account_cfg_search_account_loc).clear()
        self.find_element(*self.account_cfg_search_account_loc).send_keys(account)

        self.select(*self.account_cfg_search_state_loc).select_by_visible_text(state)

        self.select(*self.account_cfg_search_level_loc).select_by_visible_text(level)

        self.find_element(*self.account_cfg_search_button_loc).click()
        sleep(1)
        return self.find_element(*self.account_cfg_search_assert_loc).text

    def account_cfg_add_level_empty(self):
        """优先级不能为空"""
        self.account_cfg_home()

        self.find_element(*self.account_cfg_add_loc).click()
        self.switch_frame_default()
        sleep(2)
        self.find_element(*self.account_cfg_add_okbtn_loc).click()
        actualText = self.find_element(*self.account_cfg_add_okbtn_assert).text
        sleep(5)
        return actualText

    def account_cfg_add_accoun_empty(self,level="1"):
        """账号必须是5位同时包含数字和大写字母2种字符类型的组合码"""
        self.account_cfg_home()

        self.find_element(*self.account_cfg_add_loc).click()
        self.switch_frame_default()
        sleep(1)
        self.select(*self.account_cfg_add_level_loc).select_by_value(level)
        sleep(2)
        self.find_element(*self.account_cfg_add_okbtn_loc).click()
        actualText = self.find_element(*self.account_cfg_add_okbtn_assert).text
        sleep(5)
        return actualText

    def account_cfg_add_accoun_error(self,level="1",account=""):
        """账号必须是5位同时包含数字和大写字母2种字符类型的组合码"""
        self.account_cfg_home()

        self.find_element(*self.account_cfg_add_loc).click()
        self.switch_frame_default()
        sleep(1)

        self.select(*self.account_cfg_add_level_loc).select_by_value(level)

        self.find_element(*self.account_cfg_add_account_loc).clear()
        self.find_element(*self.account_cfg_add_account_loc).send_keys(account)
        sleep(2)
        self.find_element(*self.account_cfg_add_okbtn_loc).click()
        actualText = self.find_element(*self.account_cfg_add_okbtn_assert).text
        sleep(5)
        return actualText

