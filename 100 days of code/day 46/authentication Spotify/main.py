from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv('100 days of code//.gitignore')

CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
# input_date = input("What year you would like to travel to in YYYY-MM-DD format?:  ")

# response = requests.get(f"https://www.billboard.com/charts/hot-100/{input_date}")

# billboard_html = response.text

# soup = BeautifulSoup(billboard_html, 'html.parser')

# song_names_spans = soup.find_all(name="span", class_ ="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]
# print(song_names)

