from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to ChromeDriver
chrome_driver_path = './chromedriver-win64/chromedriver.exe'

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Uncomment to run Chrome in headless mode
options.add_argument('--disable-dev-shm-usage')

# Repeat the action 3 times
for _ in range(2):
    # Initialize the driver
    webdriver_service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    # Open a website
    driver.get('https://bakule.vercel.app/')

    # Wait for the element with the ID 'card' to be clickable
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    element_to_click = wait.until(EC.element_to_be_clickable((By.ID, 'card')))

    # Click the element
    element_to_click.click()

    # Keep the browser open for 5 seconds after the click
    time.sleep(1.5)


    # Close the browser
    driver.quit()
