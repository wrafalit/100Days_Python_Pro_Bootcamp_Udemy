from bs4 import BeautifulSoup
import lxml


with open("website.html", mode="r", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.a)
anchor_tag = soup.findAll(name="a")
print(anchor_tag)

for atag in anchor_tag:
    print(atag.get("href"))
    # print(atag.getText())


heading1 = soup.findAll(name="h1", id="name")
edu = soup.find(name="h4", class_="edu")
print(heading1)
print(edu.getText())

company_url = soup.select_one(selector="p a")
print(company_url)