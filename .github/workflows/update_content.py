from bs4 import BeautifulSoup

# Read the HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Modify the text
heading = soup.find("h1")
if heading:
    heading.string = "New Heading Text"
import random
paragraph = soup.find("p", id="my-paragraph") # Find paragraph by id
if paragraph:
    paragraph.string = "New paragraph text" + str(random.randint(1, 227))
    
# Save the changes
with open("index.html", "w") as file:
    file.write(str(soup))
