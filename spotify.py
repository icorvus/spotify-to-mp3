import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import re


def handle_url(url: str) -> dict:
    """Cleans url, splits it and returns dictionary with:
    - type of url
    - id of track/playlist/album
    If url is not a valid spotify link to track, playlist or album
    then type = "invalid"

    Args:
        url (str): spotify url to track, playlist or album

    Returns:
        dict: {
            "type": "track/playlist/album/invalid",
            "id": id of track/plalist/album, None when url invalid
        }
    """
    url_pattern = r"spotify.com\/(track|playlist|album)\/([A-Za-z0-9]+)"
    match = re.search(url_pattern, url)
    if match:
        if match[1] == "track":
            print(get_track_name(match[2]))
        return {
            "type": match[1],
            "id": match[2]
        }
    return {
        "type": "invalid",
        "id": None
    }


def get_track_name(id: str) -> str:
    track = sp.track(id)
    return f"{track['artists'][0]['name']} - {track['name']}"


def get_tracks_from_album(id: str) -> list:
    track_names = []
    album = sp.album_tracks(id)
    for track in album["items"]:
        artist = track["artists"][0]["name"]
        title = track["name"]
        track_name = f"{artist} - {title}"
        track_names.append(track_name)
    return track_names


def get_tracks_from_playlist(id: str) -> list:
    track_names = []
    playlist = sp.playlist_items(id)
    for item in playlist["items"]:
        artist = item["track"]["artists"][0]["name"]
        title = item["track"]["name"]
        track_name = f"{artist} - {title}"
        track_names.append(track_name)
    return track_names


# Load environment variables from .env file
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
api_credentials = SpotifyClientCredentials(client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=api_credentials)

while True:
    print(get_tracks_from_album(input("URL: ")))

get_tracks_from_playlist("4LD3f2xerFMBetFCqt124p")
