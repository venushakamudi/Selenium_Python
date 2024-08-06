import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.makemytrip.com/flights/")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath", "//span[@data-cy='closeModal']").click()
time.sleep(2)
driver.find_element("xpath", "//li[text()='Round Trip']").click()
driver.find_element("xpath", "//label[@for='departure']").click()
