# Importation des bibliothèques nécessaires
from bs4 import BeautifulSoup

# Charger votre document HTML ici
html_doc = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document HTML sur la Conquête Spatiale</title>
    <style>
        .space-highlight { color: blue; }
        #space-content { background-color: #e6e6fa; }
        article > p:first-child { font-weight: bold; }
        ul#mission-list li:nth-child(odd) { background-color: #f0f8ff; }
        div:not(.space-highlight) { color: grey; }
    </style>
</head>
<body>

<header>
    <h1>Exploration de l'Espace: Une Odyssée Moderne</h1>
</header>

<section id="space-content">
    <article>
        <h2>Les Premiers Pas sur la Lune</h2>
        <p>Ce paragraphe traite de l'atterrissage d'Apollo 11 sur la Lune en 1969.</p>
        <p class="space-highlight">Neil Armstrong fut le premier homme à marcher sur la Lune.</p>
        <p>Cette mission marqua un tournant historique dans l'exploration spatiale.</p>
    </article>

    <article>
        <h2>Mars Rover Exploration</h2>
        <p>Les rovers sur Mars ont révolutionné notre compréhension de la planète rouge.</p>
        <p>Des découvertes sur l'eau et le climat ont été faites.</p>
        <p class="space-highlight">Perseverance et Curiosity sont parmi les rovers les plus célèbres.</p>
    </article>

    <div class="space-highlight">
        La Station Spatiale Internationale est un symbole de coopération internationale dans l'espace.
    </div>

    <div>
        Les télescopes spatiaux ont permis de découvrir de nombreux exoplanètes.
    </div>

    <ul id="mission-list">
        <li>Apollo 11 - Première mission lunaire habitée</li>
        <li>Voyager - Exploration des géantes gazeuses</li>
        <li>Spitzer - Télescope spatial infrarouge</li>
        <li>Hubble - Télescope spatial observant l'univers lointain</li>
    </ul>
</section>

<footer>
    <p>Ceci est un pied de page dédié à la conquête spatiale.</p>
</footer>

</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

# Exercice 1: Extraction basée sur les Classes et ID
print("Exercice 1: Extraction basée sur les Classes et ID")
space_content = soup.find(id="space-content")
print(space_content.get_text())

space_highlights = soup.find_all("p", class_="space-highlight")
for highlight in space_highlights:
    print(highlight.get_text())

# Exercice 2: Utilisation de Pseudo-sélecteurs
print("\nExercice 2: Utilisation de Pseudo-sélecteurs")
first_child_paragraphs = soup.select("article > p:first-child")
for paragraph in first_child_paragraphs:
    print(paragraph.get_text())

odd_missions = soup.select("#mission-list li:nth-child(odd)")
for mission in odd_missions:
    print(mission.get_text())

# Exercice 3: Sélection par Négation
print("\nExercice 3: Sélection par Négation")
non_highlighted_divs = soup.select("div:not(.space-highlight)")
for div in non_highlighted_divs:
    print(div.get_text())

# Exercice 4: Sélection Combinée
print("\nExercice 4: Sélection Combinée")
article_titles = soup.select("article > h2")
for title in article_titles:
    print(title.get_text())

# Exercice 5: Challenge - Sélecteurs Complexes
print("\nExercice 5: Challenge - Sélecteurs Complexes")
second_paragraph_first_article = soup.select(
    "article:nth-of-type(1) > p:nth-of-type(2)")
if second_paragraph_first_article:
    print(second_paragraph_first_article[0].get_text())

last_mission = soup.select("#mission-list li:last-child")
if last_mission:
    print(last_mission[0].get_text())
