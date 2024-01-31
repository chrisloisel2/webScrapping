from bs4 import BeautifulSoup
import requests


url = 'https://www.blogdumoderateur.com/apple-dma-ios-app-store-safari/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'lxml')

title = soup.find_all('title', limit=1).pop().text
print(title)


for subTitle in soup.find_all('h2'):
    print(subTitle.text)


# from bs4 import BeautifulSoup

# # Remplacez ceci par votre HTML
# html_content = """<html> ... </html>"""  # Le contenu HTML va ici

# soup = BeautifulSoup(html_content, 'html.parser')

# for film in soup.find_all(class_='film'):
#     titre = film.h2.get_text()
#     avis = film.p.get_text()
#     print(f'Titre: {titre}, Avis: {avis}')
