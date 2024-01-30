from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Create a new instance of the webdriver
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Ie()
# Pour Edge, il faut télécharger le driver sur le site de Microsoft
# driver = webdriver.Edge()

# Navigate to a webpage
driver.get('http://127.0.0.1:5500/test.html')
time.sleep(2)

input = driver.find_element(
    By.CSS_SELECTOR, 'input')

input.send_keys('christopher')

button = driver.find_element(By.CSS_SELECTOR, 'button')
button.click()
