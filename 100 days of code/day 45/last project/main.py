from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")

website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())
fin = soup.find(name="div")
all_movies = soup.find_all(name = "h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open('100 days of code//day 45//last project//text.txt', 'w') as file:
    for movie in movies:
        file.write(movie + "\n")