# -*-coding:utf-8-*-
# @time       : 16/11/8 12:09
# @Author     : Zhangxy
# @File       : 001baiduSearch.py
# @Software   : PyCharm

from selenium import webdriver
import time
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium chrome 截图')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.get_screenshot_as_file("test.png")
driver.save_screenshot("111.png")
#driver.quit()
#driver.find_element_by_id('kw').send_keys('selenium')
"""
#运行chrome无界面模式
from selenium import webdriver
url = "http://demo.testfire.net"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options) #,executable_path='/Users/xxxxxx/driver/chromedirver')
driver.get('http://demo.testfire.net')
driver.quit()
"""