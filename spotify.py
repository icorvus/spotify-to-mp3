import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import re


def handle_url(url: str) -> dict:
    url_pattern = r"spotify.com\/(track|playlist|album)\/([A-Za-z0-9]+)"
    match = re.search(url_pattern, url)
    if match:
        return {
            "type": match[1],
            "id": match[2]
        }
    return {
        "type": "invalid"
    }


# Load environment variables from .env file
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
api_credentials = SpotifyClientCredentials(client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=api_credentials)

while True:
    handle_url(input("URL: "))