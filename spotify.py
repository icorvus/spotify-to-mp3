import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
api_credentials = SpotifyClientCredentials(client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=api_credentials)
