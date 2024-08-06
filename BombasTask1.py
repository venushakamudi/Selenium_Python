import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://shop.bombas.com/contact-us")
driver.maximize_window()
time.sleep(5)
message_text = driver.find_element("xpath", "//p[contains(text(),'We no longer')]").text
print(message_text)
time.sleep(2)
driver.find_element("xpath", "//button[text()='Got It']").click()
time.sleep(5)
driver.find_element("xpath", "//button[text()='Yes, Please']").click()