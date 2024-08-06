import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service("C:\\Users\\Administrator\\Downloads\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://demowebshop.tricentis.com/books")
driver.maximize_window()
time.sleep(5)

dropdown1 = driver.find_element("id", "products-orderby")
sel1 = Select(dropdown1)

for index in sel1.options:
    print(index.text)


#sel1=Select(dropdown1)
# sel1.select_by_visible_text("Price: Low to High")
#sel1.select_by_value("https://demowebshop.tricentis.com/books?orderby=5")
#select by index
#select by visible text
#select by value