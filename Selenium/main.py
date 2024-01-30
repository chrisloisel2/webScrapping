from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Chemin vers geckodriver si ce n'est pas dans PATH
# driver = webdriver.Firefox(executable_path='/chemin/vers/geckodriver')

# Si geckodriver est dans PATH
driver = webdriver.Firefox()


try:
    # Ouvrir une page web
    driver.get("https://www.lesechos.fr/")

    # attendre 5 secondes
    time.sleep(5)

    # Trouver un élément par son ID
    element = driver.find_element(
        By.CSS_SELECTOR, '#didomi-notice-agree-button')

    element.click()

    # element_by_id = driver.find_element(By.ID, "didomi-notice-agree-button")
    # Vous pouvez interagir avec l'élément, par exemple, cliquer dessus
    # element_by_id.click()

    # Trouver un élément par son nom
    # element_by_name = driver.find_element(By.NAME, "nomDeLElement")
    # Interagir avec l'élément, par exemple, entrer du texte
    # element_by_name.send_keys("Texte à entrer")

    # Trouver un élément par sa classe CSS
    # element_by_class = driver.find_element(By.CLASS_NAME, "classeDeLElement")
    # Par exemple, récupérer le texte de cet élément
    # text = element_by_class.text

    # Trouver un élément par XPath
    # element_by_xpath = driver.find_element(
    # By.XPATH, "//tag[@attribut='valeur']")
    # Cliquer sur cet élément
    # element_by_xpath.click()

    # Attendre un peu pour voir les interactions
    time.sleep(5)

except Exception as e:
    print(f"Une erreur est survenue : {e}")
finally:
    # Fermer le navigateur
    driver.quit()

# Les différents Facons de trouver un élément
# driver.find_element_by_id("id")
# driver.find_element_by_name("name")
# driver.find_element_by_class_name("class")
# driver.find_element_by_tag_name("tag")
# driver.find_element_by_css_selector("css_selector")
# driver.find_element_by_xpath("xpath")
# driver.find_element(By.ID, "id")
# driver.find_element(By.NAME, "name")
# driver.find_element(By.CLASS_NAME, "class")
# driver.find_element(By.TAG_NAME, "tag")
# driver.find_element(By.CSS_SELECTOR, "css_selector")
# driver.find_element(By.XPATH, "xpath")
# driver.find_elements(By.XPATH, "//input")
# driver.find_elements(By.XPATH, "//input[@type='text']")
# driver.find_elements(By.XPATH, "//input[@type='text'][@name='name']")
# driver.find_elements(By.XPATH, "//input[@type='text' or @name='name']")

# Evenement sur un élément
# element = driver.find_element_by_id("id")
# element.click()

# element = driver.find_element_by_id("id")
# element.send_keys("Hello World!")


# driver.close()

# Fermer le navigateur
