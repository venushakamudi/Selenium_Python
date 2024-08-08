import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(2)
#driver.save_screenshot("C:\\Users\\Plabani\\Documents\\MY\\DEMO\\screen.jpeg")
S1=lambda  X:driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S1('Width'),S1('Height'))
driver.find_element("tag name","body").screenshot("C:\\Users\\Venu\\screenshot_selenium.png")