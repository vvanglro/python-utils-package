# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 17:20
# @Author  : wanghao
# @File    : pyppeteer挂代理.py
# @Software: PyCharm
import time
import tkinter
from fake_useragent import UserAgent
from pyppeteer import launch
import asyncio


async def main(url):
    p = Proxies() # 获取代理的func
    print(p)  # 代理func返回的信息('http://ip:host', {'username': 'username', 'password': '123456'})
    
    # "headless":False 有界面模式
    # "userDataDir":r"./temp" 自己设置临时数据目录  这样不会报错OSError: Unable to remove Temporary User Data
    browser = await launch(headless=False,
                           userDataDir=r"./temp",
                           args=[
        '--disable-infobars', # 关闭自动化提示框
        "--proxy-server=" + p[0], # 代理
        '--start-maximized', # 窗口最大化
    ]
                           )   # headless=True 启动了无头模式，--proxy-server 启动了代理
    page = await browser.newPage()  # 创建新页面并返回对象
    # 设置请求头userAgent
    await page.setUserAgent(
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36')
    await page.authenticate(p[1])          # 输入代理账号密码
    # await page.setExtraHTTPHeaders(Proxies())            # 在pyppeteer中和puppeteer是一样的，都不能把隧道加在args里，只能加在headers里

    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                   '{ webdriver:{ get: () => false } }) }')  # 本页刷新后值不变 去掉网站对webdriver的检测

    # 查看当前 桌面视图大小
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    print(f'设置窗口为：width：{width} height：{height}')

    # 设置网页 视图大小
    await page.setViewport(viewport={'width': width, 'height': height})

    await page.goto(url, {
        'timeout': 1000*8  # 这里设置超时8秒
    })

    await asyncio.sleep(4)

    html = await page.content()  # 返回页面源码
    # print(html)

    await browser.close()

    return html


def bb():

    loop = asyncio.get_event_loop()
    done= loop.run_until_complete(main('https://bot.sannysoft.com/'))
    print(done)
    # for task in done:

if __name__ == '__main__':
    bb()
