from bs4 import BeautifulSoup
import requests

respons = requests.get("https://news.ycombinator.com/news")

vc_web_page = respons.text

soup = BeautifulSoup(vc_web_page, "html.parser")
# print(soup.title)

articles = soup.find_all(name="a", class_="titlelink")
article_text = []
article_link = []
for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)


score_article = [score.getText() for score in soup.find_all(name="span", class_="score")]
scores = [int(score.split()[0]) for score in score_article]


max_score = scores.index(max(scores))
print(article_text[max_score])
print(article_link[max_score])
print(scores[max_score])