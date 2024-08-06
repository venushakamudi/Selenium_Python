import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath", "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element("xpath", "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element("xpath", "//button[@type='submit']").click()
time.sleep(5)
driver.close()