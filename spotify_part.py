import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = '5aa1088be7d448a5970906632adf3c52'
client_secret = 'c8144353448e4ef6b48acbb1e8c8444f'
redirect_uri = 'http://localhost:8888/callback'

scope = 'user-read-playback-state user-modify-playback-state user-library-read'

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

play_playlist_by_mood("confident") 
