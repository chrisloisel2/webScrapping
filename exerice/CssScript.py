from bs4 import BeautifulSoup
import requests

# Make a request to the website
html = """
<div class="table">
	<apple />
	<apple />
	<plate>
	<apple />
	</plate>
	<plate />
</div>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Use BeautifulSoup to parse the HTML and extract the data
# Add your code here to navigate and extract data from the HTML

# Print the extracted data
print(soup.prettify())

print(soup.select("apple:nth-of-type(2)"))
