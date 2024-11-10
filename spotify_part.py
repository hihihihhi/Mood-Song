import json
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

client_id = '5aa1088be7d448a5970906632adf3c52'
client_secret = 'c8144353448e4ef6b48acbb1e8c8444f'
redirect_uri = 'http://localhost:8888/callback'

scope = 'user-read-playback-state user-modify-playback-state user-library-read user-read-currently-playing'


def create_spotify_object():
    oauth_object = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
    try:
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']
        return spotipy.Spotify(auth=token)
    except spotipy.oauth2.SpotifyOauthError as e:
        print("Error during authorization:", e)
        return None

def play_playlist_by_mood(mood):
    oauth_object = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

    try:
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']
    except spotipy.oauth2.SpotifyOauthError as e:
        print("Error during authorization:", e)
        return
    
    spotifyObject = spotipy.Spotify(auth=token)

    results = spotifyObject.search(q=f"{mood} mix", type="playlist", limit=20)
    playlists = results['playlists']['items']

    spotify_playlists = [playlist for playlist in playlists if playlist['owner']['id'] == 'spotify']

    if spotify_playlists:
        selected_playlist = spotify_playlists[0]

        devices = spotifyObject.devices()
        device_list = devices['devices']
        
        if device_list:
            device_id = device_list[0]['id']
            
            spotifyObject.start_playback(device_id=device_id, context_uri=selected_playlist['uri'])
            print(f"Playing playlist: {selected_playlist['name']}")
        else:
            print("No active Spotify device found. Please open Spotify on a device and try again.")
    else:
        print(f"No playlists found for the mood: {mood}")


def get_duration(spotifyObject):
    current_playback = spotifyObject.current_playback()
    return current_playback['item']['duration_ms']

def get_time(spotifyObject):
    current_playback = spotifyObject.current_playback()
    return current_playback['progress_ms']

def get_remaining_time_in_song(spotifyObject):
    current_playback = spotifyObject.current_playback()
    if current_playback and current_playback['is_playing']:
        progress_ms = current_playback['progress_ms']
        duration_ms = current_playback['item']['duration_ms']
        remaining_time_ms = duration_ms - progress_ms
        return remaining_time_ms / 1000  # Convert to seconds
    else:
        print("No song currently playing.")
        return None


