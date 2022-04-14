from datetime import datetime
import requests
from bs4 import BeautifulSoup

if False:
    data_user = input("Which year do you want to travel to? type the date in this format, YYYY-MM-DD : ")
else:
    data_user = "2000-01-01"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{data_user}/")

user_hot_web = response.text

soap = BeautifulSoup(user_hot_web, "html.parser")
# print(soap.prettify())

# for title in soap.find_all(name="h3", id="title-of-a-story"):
#     print(title.getText().strip())

artist_list = [artist.getText().strip() for artist in soap.find_all(name="span", class_="a-no-trucate")]
print(len(artist_list))

