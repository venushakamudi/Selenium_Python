from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()

try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable("name","submit")
    )
    print("element is clickable")
except:
    print("element is not clickable")