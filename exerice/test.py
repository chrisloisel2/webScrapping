# Utilisation de la librairie Request Pour faire mon premier appel HTTP
import requests

# Inporter BeautifulSoup, qui va nous permettre de parser le HTML

from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/Spacial.html"


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

rovers = soup.select("article:nth-of-type(2) > :not(p)")[0]

for parent in rovers.parent:
	print(parent)

print(rovers)

# films = body.find('div', attrs={'class': 'film'})
# print(films)
# for film in films:
#     title = film.find('h2')
#     avis = film.find('p')
#     print(title, avis)

# Afficher le titre de la page

# soup.find('ul')
# ul = soup.find('ul')

# h2 = soup.find('h2')

# trouver tous les h2
# body = soup.find('body')

# trouver tous les h2
# p = body.find_all('h1', attrs={'id': 'Titre'}, limit=2)
# print(p)

# mainTitle = soup.find('span', attrs={'class': 'mw-page-title-main'})
# print(mainTitle.text)

# Creer une liste de film, chaque film aura son titre scrappé sur le document donné,
# Votre liste de film devra etre une liste de tuple (titre, avis),
# Vous renseignerez l'avis de chaque film.
#  Je ne veux que les 5 premiers films de la liste.
