import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath", "//input[@name='FirstName']").send_keys("Venu")
driver.find_element("xpath", "//input[@name='LastName']").send_keys("Shakamudi")
driver.find_element("xpath", "//input[@name='Email']").send_keys("Venu@gmail.com")
driver.find_element("xpath", "//input[@name='Password']").send_keys("Venu123")
driver.find_element("xpath", "//input[@name='ConfirmPassword']").send_keys("Venu123")
driver.find_element("xpath", "//input[@type='submit']").click()
time.sleep(5)
driver.close()