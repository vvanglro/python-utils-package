# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 10:49
# @Author  : wanghao
# @File    : 自动下载selenium驱动.py
# @Software: PyCharm

# pip install webdriver-manager	 -i https://pypi.douban.com/simple

import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

os.environ['WDM_LOG_LEVEL'] = '0'   # 取消日志的输出
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'  # 取消换行
# https://gitee.com/zmister/MrDoc/blob/master/app_doc/report_html2pdf.py
# https://www.cnblogs.com/zibinchen/p/14310637.html

driver = webdriver.Chrome(
    ChromeDriverManager(
        path='./driver/', # 设置驱动下载保存地址
        url='https://npm.taobao.org/mirrors/chromedriver/',  # 设置国内下载源
        latest_release_url='https://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE',  # 设置国内下载源
).install())

driver.close()
driver.quit()
