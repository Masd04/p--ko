from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-gpu')  # Applicable to windows os only
options.add_argument('--disable-extensions')

# Repeat the action 2 times
for _ in range(1):
    # Initialize the driver
    driver = webdriver.Chrome(options=options)

    # Open a website
    driver.get('https://bakule.vercel.app/')

    # Wait for the element with the ID 'card' to be clickable
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    element_to_click = wait.until(EC.element_to_be_clickable((By.ID, 'card')))

    # Click the element
    element_to_click.click()

    # Keep the browser open for 1.5 seconds after the click
    time.sleep(1.5)

    # Close the browser
    driver.quit()
