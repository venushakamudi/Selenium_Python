from selenium import webdriver

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option(name= "detach", value= True)
# s = Service('C:\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome('C:\\chromedriver-win64\\chromedriver.exe')



driver.get("https://webflow.com/made-in-webflow/mouse-hover")