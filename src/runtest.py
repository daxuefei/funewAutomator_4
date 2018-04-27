# coding:utf-8
__auth__='wangshuyuan'
'''
description:执行测试
'''
import unittest,time
from lib import HTMLTestRunner
from config.globalparameter import test_case_path,report_name
from src.common import send_mail

#构建测试集，包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')

#执行测试
if __name__=="__main__":
    report = report_name+"Report.html"
    fb=open(report,'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'放牛娃自动化测试报告',
        description=u'项目描述：生产环境',
        verbosity=2
    )
    runner.run(suite)
    fb.close()
    #发送邮件
    # time.sleep(10)
    # email =send_mail.send_email()
    # email.sendReport()