# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 10:15
# @Author  : wanghao
# @File    : 将页面转为pdf.py
# @Software: PyCharm
from selenium import webdriver
import json, base64
from webdriver_manager.chrome import ChromeDriverManager
import os

os.environ['WDM_LOG_LEVEL'] = '0'   # 取消日志的输出
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'  # 取消换行

def send_devtools(driver, cmd, params={}):
  resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
  url = driver.command_executor._url + resource
  body = json.dumps({'cmd': cmd, 'params': params})
  response = driver.command_executor._request('POST', url, body)
  # print(response)
  if not response:
      raise Exception(response.get('value'))
  return response.get('value')

def save_as_pdf(driver, path, options={}):
  # https://timvdlippe.github.io/devtools-protocol/tot/Page#method-printToPDF
  result = send_devtools(driver, "Page.printToPDF", options)   # 将页面存为pdf
  with open(path, 'wb') as file:
    file.write(base64.b64decode(result['data']))


options = webdriver.ChromeOptions()
options.add_argument("--headless") # 浏览器不提供可视化页面
options.add_argument("--disable-gpu") # 不用gpu
options.add_argument('--no-sandbox')  # 不使用沙箱
options.add_argument('--disable-dev-shm-usage') # 禁止使用/dev/shm，防止内存不够用
options.add_argument("--start-maximized")  # 最大化运行（全屏窗口）,不设置，取元素会报错

driver = webdriver.Chrome(
    ChromeDriverManager(
        path='./driver/', # 设置驱动下载保存地址
        url='https://npm.taobao.org/mirrors/chromedriver/',  # 设置国内下载源
        latest_release_url='https://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE',  # 设置国内下载源
).install(),options=options)
driver.get("https://www.baidu.com/")

save_as_pdf(driver, r'page.pdf', {  'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'preferCSSPageSize': True, })
