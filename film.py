from bs4 import BeautifulSoup
import requests  # Import manquant pour utiliser requests.get

url2 = "http://127.0.0.1:5500/webScrapping/films.html"

request2 = requests.get(url2)
html2 = """
<html>
<head>
    <title>Liste de films</title>
	<style>
		div > h2 {
			background-color: red;
		}
	</style>
</head>
<body>
	<h2>Le Parrain</h2>
    <div class="film">
        <p>Avis: Un classique du cinéma.</p>
    </div>
    <div class="film">
        <h2>Inception</h2>
        <p>Avis: Un film captivant et complexe.</p>
    </div>
    <div class="film">
        <h2>Intouchables</h2>
        <p>Avis: Une histoire d'amitié touchante.</p>
    </div>
	<div class="film">
		<h2>Le Parrain</h2>
		<p>Avis: Un classique du cinéma.</p>
	</div>
	<div class="film">
		<h2>Inception</h2>
		<p>Avis: Un film captivant et complexe.</p>
	</div>
	<div class="film">
		<h2>Intouchables</h2>
		<p>Avis: Une histoire d'amitié touchante.</p>
	</div>
</body>
</html>
"""
soup2 = BeautifulSoup(html2, 'html.parser')

listfilm = []

liste = soup2.find_all('div', limit=5, attrs={"class": "film"})
for film in liste:
    lis = film.find('h2')
    print(lis)
