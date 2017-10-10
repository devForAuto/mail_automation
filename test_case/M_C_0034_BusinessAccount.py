#-*- coding:utf-8 -*-

from test_case.A_PublicLogin import is_login
import unittest
from test_case.page_obj.Page_0034_BusinessAccount import MailBusinessAccount
from util import randomUtil

class BusinessAccount(unittest.TestCase):
    dr=is_login()
    flag = False
    account = randomUtil.getRandomUpperInt(5)
    print(account)
    def setUp(self,driver=dr):
        self.driver=driver
        self.home=MailBusinessAccount(self.driver)

    def test_0001_account_cfg_home(self):
        """业务帐号管理主页面"""
        self.home.account_cfg_home()

    def test_0002_account_cfg_add(self):
        """添加帐号"""
        password=randomUtil.getRandomStrInt(8)
        hint = self.home.account_cfg_add(level="1",account=self.account,passa=password,confirmPass=password)
        print(hint)
        self.assertEqual(hint, self.account)

    def test_0003_account_cfg_search(self):
        """搜索帐号"""
        hint = self.home.account_cfg_search(account=self.account,state="全部",level="全部")
        print(hint)
        self.assertEqual(hint,self.account)

    def test_0004_account_cfg_add_level_empty(self):
        """优先级不能为空"""
        hint = self.home.account_cfg_add_level_empty()
        self.assertEqual(hint, "优先级不能为空")

    def test_0005_account_cfg_add_account_empty(self):
        """账号不能为空校验"""
        hint = self.home.account_cfg_add_accoun_empty()
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0006_account_cfg_add_account_error(self):
        """账号必须是5位校验，输入4位"""
        hint = self.home.account_cfg_add_accoun_error(account=randomUtil.getRandomUpperInt(4))
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0007_account_cfg_add_account_error(self):
        """账号必须是5位校验，输入6位"""
        print('\n')
        account = randomUtil.getRandomUpperInt(6)
        print(account)
        hint = self.home.account_cfg_add_accoun_error(account=account)
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0008_account_cfg_add_account_error(self):
        """账号必须是包含数字和大写字母，只输入数字"""
        print('\n')
        account = randomUtil.getRandomInt(5)
        print(account)
        hint = self.home.account_cfg_add_accoun_error(account=account)
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0009_account_cfg_add_account_error(self):
        """账号必须是包含数字和大写字母，只输入大写字母"""
        print('\n')
        account = randomUtil.getRandomUpperStr(5)
        print(account)
        hint = self.home.account_cfg_add_accoun_error(account=account)
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0010_account_cfg_add_account_error(self):
        """账号必须是包含数字和大写字母，只输入数字+小写字母"""
        print('\n')
        account = randomUtil.getRandomInt(3) + randomUtil.getRandomLowerStr(2)
        print(account)
        hint = self.home.account_cfg_add_accoun_error(account=account)
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0011_account_cfg_add_account_error(self):
        """账号必须是包含数字和大写字母，只输入大写字母+小写字母"""
        print('\n')
        account = randomUtil.getRandomUpperInt(3) + randomUtil.getRandomLowerStr(2)
        print(account)
        hint = self.home.account_cfg_add_accoun_error(account=account)
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_0012_account_cfg_add_account_error(self):
        """账号必须是包含数字和大写字母，只输入汉字"""
        print('\n')
        account = randomUtil.getRandomChine(5)
        print(account)
        hint = self.home.account_cfg_add_accoun_error(account=account)
        self.assertEqual(hint, "账号必须是5位同时包含数字和大写字母2种字符类型的组合码")

    def test_z_logout(self):
        """退出"""
        print("退出成功")
        self.flag = True

    def tearDown(self):
        # print(self.flag)
        if self.flag:
            self.driver.quit()
        else:
            self.driver.refresh()

if __name__ == "__main__":
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(BusinessAccount("test_0006_account_cfg_add_account_error"))
    #
    # runner=unittest.TextTestRunner()
    # runner.run(suite)