from bs4 import BeautifulSoup

# Read the HTML file
with open("index.html", "r") as file:
    content = file.read()

# Parse the HTML
soup = BeautifulSoup(content, "html.parser")

# Modify the text
import random
paragraph = soup.find("p", id="updating") # Find paragraph by id
if paragraph:
    paragraph.string = "Updating Number = " + str(random.randint(1, 227))
    
# Save the changes
with open("index.html", "w") as file:
    file.write(str(soup))

