import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()
time.sleep(2)

src = driver.find_element("xpath", "//img[@id='angular']")
target = driver.find_element("xpath", "//div[@id='droparea']")

act = ActionChains(driver)
act.drag_and_drop(src, target).perform()