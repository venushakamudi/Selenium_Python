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

driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.find_element("name","cusid").send_keys(123)
driver.find_element("name","submit").click()
a=Alert(driver)
print(a.text)
a.accept()
#a.dismiss()