# coding:utf-8
__auth__='wangshuyuan'
'''
description:测试登录功能
'''
from appium import webdriver
import unittest
from src.pages import login_page
from src.common import gesture_mainpulation
from src.common import driver_configure

class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_mainpulation.gesture_mainpulation()

    def test_01login(self):
        '''测试登录功能'''
        #登录页

        self.login_page = login_page.login_page(self.driver)
        self.login_page.input_user("15370135956")
        self.login_page.input_Pws("123456")
        self.login_page.click_btnLogin()



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()