from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.toutiao.com/")
for i in range(5):
    time.sleep(10)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')