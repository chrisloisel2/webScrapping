from bs4 import BeautifulSoup
import requests

# Make a request to the website
url = "https://fr.wikipedia.org/wiki/Barcelone"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")


# myentreprise = soup.select("table > tr:nth-of-type(2)")

# for entreprise in myentreprise:
# 	name = entreprise.select("td:nth-of-type(1)")[0].get_text()
# 	price = entreprise.select("td:nth-of-type(2)")[0].get_text()
# 	change = entreprise.select("td:nth-of-type(3)")[0].get_text()
# 	print(f"Nom: {name}, Prix: {price}, Changement: {change}")


lien = soup.select("a")[0]['href']
print(lien)
