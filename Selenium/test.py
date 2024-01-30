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
driver.get('https://fr.wikipedia.org/wiki/Paris')

# Perform actions on the webpage
# ...
# Titre de la page
# titre = driver.find_element(By.ID, 'firstHeading')

# titre = driver.find_element(By.XPATH, '//a[@href="/wiki/Gentil%C3%A9"]')
# titre = driver.find_element(By.CSS_SELECTOR, '#firstHeading')
Pays = driver.find_element(By.CSS_SELECTOR, 'a[href="/wiki/France"]')
print(Pays.text)

# Sleep de 5 secondes
time.sleep(1)


# Close the webdriver
driver.quit()
