from selenium import webdriver
import time
#driver = webdriver.Firefox(executable_path = '/Users/kun/Downloads/geckodriver')
driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium chrome 截图')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.get_screenshot_as_file("test.png")
driver.save_screenshot("111.png")
#driver.quit()