from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.headless = True  # Run in headless mode
# Add any other necessary options here

for _ in range(1):
# Selenium 4.x uses the 'options' argument instead of 'desired_capabilities'
    s = Service('chromedriver-win64/chromedriver.exe')  # Specify path to chromedriver if not in PATH
    driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)

driver.get("https://commuplat.vercel.app/")
print(driver.title)

# Wait for the element with the ID 'card' to be clickable
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
element_to_click = wait.until(EC.element_to_be_clickable((By.ID, 'card')))

    # Click the element
element_to_click.click()



    # Keep the browser open for 10 seconds after the click
time.sleep(10)

print(driver.title)

    # Close the browser
driver.quit()
