from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set up selenium to connect to the service container
selenium_grid_url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(
    command_executor=selenium_grid_url,
    desired_capabilities=DesiredCapabilities.CHROME,
)

driver.get("http://www.google.com")
print(driver.title)
driver.quit()
