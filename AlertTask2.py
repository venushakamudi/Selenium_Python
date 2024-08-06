import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()
a=Alert(driver)
print(a.text)
a.accept()
time.sleep(5)
driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
b=Alert(driver)
print(b.text)
b.dismiss()
time.sleep(5)
driver.find_element("xpath", "//button[text()='Click for JS Prompt']").click()
c=Alert(driver)
print(c.text)
c.send_keys("1234")
c.accept()