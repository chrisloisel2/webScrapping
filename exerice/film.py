from bs4 import BeautifulSoup
import requests  # Import manquant pour utiliser requests.get

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
        <p id='main'>Avis: Un film captivant et complexe.</p>
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
    # recupere le titre de chaque film
    titre = film.select('p', id='main')[0].text

    print(titre)
