from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
print(driver.title)
driver.quit()
