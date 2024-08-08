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

driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(5)

element = driver.find_element("xpath", "//span[text()='Apple iPad (10th generation): with A1…']")
driver.execute_script("arguments[0].scrollIntoView();", element)