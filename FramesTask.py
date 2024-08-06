import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath", "//span[text()='Hello, sign in']").click()
driver.find_element("id", "ap_email_login").send_keys('+919390293370')
driver.find_element("id", "continue").click()
time.sleep(2)
driver.find_element("id", "ap_password").send_keys('VENU@amazon')
driver.find_element("id", "signInSubmit").click()
time.sleep(5)
search_box = driver.find_element("id", "twotabsearchtextbox")
search_box.send_keys("Mobiles under 10000")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element("xpath", "(//button[text()= 'Add to cart'])[1]").click()
time.sleep(10)
driver.find_element("id", "nav-cart-count").click()
driver.find_element("name", "proceedToRetailCheckout").click()
time.sleep(10)
driver.find_element("xpath", "//span[@id='shipToThisAddressButton']").click()
time.sleep(5)
driver.find_element("xpath", "//input[@value='SelectableAddCreditCard']").click()
driver.find_element("xpath", "(//a[contains(text(),'Enter card details')])[1]").click()
time.sleep(2)
driver.switch_to.frame(0)
driver.find_element("name", "addCreditCardNumber").send_keys('1234 5678 1234 5678')