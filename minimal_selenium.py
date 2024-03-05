from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.headless = True  # Run in headless mode
# Add any other necessary options here

# Selenium 4.x uses the 'options' argument instead of 'desired_capabilities'
s = Service('chromedriver-win64/chromedriver.exe')  # Specify path to chromedriver if not in PATH
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)

driver.get("http://www.google.com")
print(driver.title)
driver.quit()
