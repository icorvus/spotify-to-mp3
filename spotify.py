import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import re


def handle_url(url: str) -> list:
    """Cleans url, splits it and calls appropriate function which
    returns a list of tracks

    Args:
        url (str): spotify url to track, playlist or album

    Returns:
        list: list of track names
    """
    url_pattern = r"spotify.com\/(track|playlist|album)\/([A-Za-z0-9]+)"
    match = re.search(url_pattern, url)
    if match:
        type = match[1]
        id = match[2]
        if type == "track":
            return get_track_name(id)
        if type == "playlist":
            return get_tracks_from_playlist(id)
        if type == "album":
            return get_tracks_from_album(id)
    return []


def get_track_name(id: str) -> list:
    """Get track name given id of song

    Args:
        id (str): id of song

    Returns:
        list: single element list containing track name
    """
    track = sp.track(id)
    return [f"{track['artists'][0]['name']} - {track['name']}"]


def get_tracks_from_album(id: str) -> list:
    """Get track names given id of album

    Args:
        id (str): id of album

    Returns:
        list: list containing track names of all songs found on album
    """
    track_names = []
    album = sp.album_tracks(id)
    for track in album["items"]:
        artist = track["artists"][0]["name"]
        title = track["name"]
        track_name = f"{artist} - {title}"
        track_names.append(track_name)
    return track_names


def get_tracks_from_playlist(id: str) -> list:
    """Get track names given id of playlist

    Args:
        id (str): id of playlist

    Returns:
        list: list containing track names of all songs found on playlist
    """
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

# Authenticate API
api_credentials = SpotifyClientCredentials(client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=api_credentials)
