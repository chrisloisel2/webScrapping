from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Create a new instance of the WebDriver
driver = webdriver.Firefox()

# Now you can start using Selenium methods on the driver object
# For example, let's navigate to a website
driver.get('https://www.pathe.fr/')

boutonCookie = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located(
	    (By.CSS_SELECTOR, "#didomi-notice-agree-button"))
)

boutonCookie.click()

boutonSearch = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, ".link-icon--transparent"))
)

print(boutonSearch.get_attribute("role"))
print(boutonSearch.text)

boutonSearch.click()

input = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='search-global']"))
)

input.send_keys('star wars')

input.send_keys(Keys.RETURN)

time.sleep(5)

# Close the WebDriver
driver.quit()
