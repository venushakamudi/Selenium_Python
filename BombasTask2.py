import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://shop.bombas.com")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath", "//button[text()='Got It']").click()
time.sleep(5)
driver.find_element("xpath", "//span[@data-name='close']").click()
time.sleep(2)
driver.find_element("xpath", "(//a[text()='Kids'])[1]").click()
time.sleep(2)
driver.find_element("xpath", "//i[contains(text(),'0-6 or 6-12')]").click()
time.sleep(2)
driver.find_element("xpath", "//h4[text()='Baby Socks 4-Pack (0-6 Months) ']").click()
time.sleep(2)
driver.find_element("xpath", "//button[text()='Add to Bag']").click()
time.sleep(5)
driver.find_element("xpath","//button[@data-track-label='Cart']").click()
time.sleep(2)
driver.find_element("xpath", "//button[@data-testid='ProductVariant_trash-button']")