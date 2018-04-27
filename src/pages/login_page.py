

import time

# coding:utf-8
__author__ = 'wangshuyuan'
'''
 description:登录页
'''
from src.common import Base_page
from appium.webdriver.common import mobileby


class login_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    etUser_loc = (by.ID,"com.xiniunet.xntalk:id/et_account")
    etPws_loc = (by.ID,"com.xiniunet.xntalk:id/et_password")
    btnLogin_loc = (by.ID,"com.xiniunet.xntalk:id/btn_login")

    def input_user(self,username):
        self.send_keys(username,*self.etUser_loc)

    def input_Pws(self,password):
        self.send_keys(password,*self.etPws_loc)

    def click_btnLogin(self):
        self.find_element(*self.btnLogin_loc).click()
        time.sleep(10)