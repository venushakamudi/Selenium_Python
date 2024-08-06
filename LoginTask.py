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
driver.find_element("xpath", "//a[text()='Log in']").click()
driver.find_element("xpath", "//input[@name='Email']").send_keys("venushakamudi@gmail.com")
driver.find_element("xpath", "//input[@name='Password']").send_keys("Venu123")
driver.find_element("xpath", "//input[@value='Log in']").click()
time.sleep(5)
driver.find_element("xpath", "(//input[@value='Add to cart'])[2]").click()
time.sleep(5)
driver.find_element("xpath", "//span[contains(text(),'Shopping')]").click()
time.sleep(2)
driver.find_element("xpath", "//div[@class='terms-of-service']//input[@type='checkbox']").click()
driver.find_element("xpath", "//button[@name='checkout']").click()