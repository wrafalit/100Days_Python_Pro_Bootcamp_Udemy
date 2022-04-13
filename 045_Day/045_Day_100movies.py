import requests
from bs4 import BeautifulSoup

respons = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_web = respons.text

soap = BeautifulSoup(empire_web, "html.parser")

all_movies = soap.find_all(name="h3", class_="title")
print(all_movies)
