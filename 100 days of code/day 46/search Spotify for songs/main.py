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
        cache_path="100 days of code//day 46//search Spotify for songs//token.txt"
    )
)

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_html = response.text
soup = BeautifulSoup(billboard_html, 'html.parser')
song_names_spans = soup.find_all(name="span", class_ ="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard TOP 100",
    public=False,
    description="A playlist I created with Python"
)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)