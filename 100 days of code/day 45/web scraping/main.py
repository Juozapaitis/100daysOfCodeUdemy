from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_ = "score")]

print(article_upvotes)
largest_number_index = article_upvotes.index(max(article_upvotes))
print(f"{article_texts[largest_number_index]}: {article_links[largest_number_index]}")

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# for tag in article_tags:
#     print(tag.getText())

