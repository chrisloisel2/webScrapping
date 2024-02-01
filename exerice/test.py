# Utilisation de la librairie Request Pour faire mon premier appel HTTP
import requests

# Inporter BeautifulSoup, qui va nous permettre de parser le HTML

from bs4 import BeautifulSoup


chaineHTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="UTF-8">
	<title>Test</title>
	<title>Test</title>
</head>
<body>
	<h1>Titre principal</h1>
	<h1 id="main">Test</h1>

	<h2 class="hfdus fjdsif zabd e dqsd">Titre secondaire</h2>
	<p>Paragraphe</p>
	<h2 class="hfdus fjdsif zabd e dqsd">Titre terciaire</h2>
	<ul>
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
	</ul>
	<h2 class="hfdus fjdsif zabd e dqsd">Titre terciaire</h2>
	<a href="https://www.google.fr">Lien vers google</a>
 </body>
</html>
"""

url = "https://www.allocine.fr/film/meilleurs/"

reponse = requests.get(url)

# Utiliser beautifulSoup pour parser le HTML
soup = BeautifulSoup(chaineHTML, 'html.parser')

print(soup.prettify(), "\n\n\n")

# recuperer une balise p grace a BeautifulSoup

p = soup.find('p')
print("premier P :", p)

p2 = soup.h1
print("second P :", p2)

# Recuperer toutes les balises d'un certain tag

p3 = soup.find_all('li')
print("troisieme P :", p3)


p4 = soup.select('li')
print("quatrieme P :", p4)


# Recuperer une balise via son ID

h1 = soup.find('h1', attrs={'id': 'main'})
print("premier h1 :", h1)

h2 = soup.find_all(attrs={'class': 'hfdus fjdsif zabd e dqsd'})
print("premier h2 :", h2)

h3 = soup.select('h2.hfdus.fjdsif.zabd.e.dqsd')
print("premier h3 :", h3)
for h in h3:
	print(h.text)


# Recuperer le contenu d'une balise


print("Contenu de h1 :", h1.text)


# Recuperer les attributs d'une balise

lien = soup.find('a')
print("lien :", lien.attrs['href'])


ul = soup.find('ul')

for child in ul.children:
	print(child)

for parents in ul.parents:
	print(parents)

for sibling in ul.next_siblings:
	print(sibling)

# rovers = soup.select("article:nth-of-type(2) > :not(p)")[0]

# for parent in rovers.parent:
# 	print(parent)

# print(rovers)

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
