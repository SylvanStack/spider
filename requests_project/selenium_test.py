# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys #导入Keys类
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Chrome()
# try:
#     browser.get(' https://www.baidu.com')   # 请求页面
#     input = browser.find_element_by_id('kw')  #查询节点
#     input.send_keys('Python') # 输入框中输入“Python”
#     input.send_keys(Keys.ENTER) #回车功能
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url) # 当前url
#     print(browser.get_cookies()) #前Cookies
#     print(browser.page_source) # 获取代码
# finally:
#     browser.close() # 页面关闭


# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# print(browser.page_source)
# browser.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# find_element()
