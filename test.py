# Utilisation de la librairie Request Pour faire mon premier appel HTTP
import requests

# Inporter BeautifulSoup, qui va nous permettre de parser le HTML

from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/test.html"


# chaineHTML = """
# <!DOCTYPE html>
# <html lang="fr">
# <head>
# 	<meta charset="UTF-8">
# 	<title>Test</title>
# 	<title>Test</title>
# </head>
# <body>
# 	<h1>Titre principal</h1>

# 	<h2>Titre secondaire</h2>
# 	<p>Paragraphe</p>
# 	<h2>Titre terciaire</h2>
# 	<ul>
# 		<li>Item 1</li>
# 		<li>Item 2</li>
# 		<li>Item 3</li>
# 	</ul>
#  </body>
# </html>
# """

request = requests.get(url)

html = request.content

# Utiliser beautifulSoup pour parser le HTML
soup = BeautifulSoup(html, 'html.parser')

# Afficher le titre de la page

# soup.find('ul')
ul = soup.find('ul')

h2 = soup.find('h2')

# trouver tous les h2
h2 = soup.find_all('h2')

# Iterrer sur les h2
for div in h2:
	print(div.text)
