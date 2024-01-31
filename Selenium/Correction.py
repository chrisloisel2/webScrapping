from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Firefox()
driver.get("https://www.lesechos.fr/")
# # Ouvrir une nouvelle fenêtre
# driver.execute_script("window.open('');")

# # Lister les différentes fenêtres ouvertes
# print(driver.window_handles)
# handles = driver.window_handles

# # Changer de fenêtre
# driver.switch_to.window(handles[1])

# time.sleep(5)

# driver.switch_to.window(handles[0])

try:

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[id="didomi-notice-agree-button"]'))
    )
    button.click()

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[aria-label='Recherche']")
        )
    )
    search_box.click()

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input")
        )
    )
    search_box.send_keys("intelligence artificielle")

    search_box.send_keys(Keys.RETURN)

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
    )
    articles = driver.find_elements(By.CSS_SELECTOR, "article")

    print(len(articles))

    for article in articles[:10]:  # Limite à 10 articles
        lien = article.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        print(lien)
        driver.execute_script("window.open('');")

    time.sleep(50)


finally:
    driver.quit()

print("Extraction terminée. Les données sont enregistrées dans 'les_echos_articles.csv'")
