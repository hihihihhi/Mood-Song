import json
import spotipy
import webbrowser

username = 'aryan'
client_id = 'ab090a58301b4f05ae24cfd5b62ba169'
client_secret = '0fa9c5cc24a948e28e9a0ec4d104ccd7'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(client_id, client_secret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

# To print the response in readable format. 
print(json.dumps(user_name, sort_keys=True, indent=4)) 

def find_spotify_playlist(mood):
    results = spotifyObject.search(q=f"{mood} mix", type="playlist", limit=20)
    playlists = results['playlists']['items']
    # Filter playlists to include only those created by Spotify
    spotify_playlists = [playlist for playlist in playlists if playlist['owner']['id'] == 'spotify']
    
    return spotify_playlists

while True: 
    print("Welcome to the project, " + user_name['display_name']) 
    print("0 - Exit the console") 
    print("1 - Search for a Song") 
    print("2 - Find Playlists by Mood")  # Added this option for mood-based playlist search
    user_input = int(input("Enter Your Choice: ")) 

    if user_input == 1: 
        search_song = input("Enter the song name: ") 
        results = spotifyObject.search(search_song, 1, 0, "track") 
        songs_dict = results['tracks'] 
        song_items = songs_dict['items'] 
        song = song_items[0]['external_urls']['spotify'] 
        webbrowser.open(song) 
        print('Song has opened in your browser.') 

    elif user_input == 2: 
        mood = input("Enter the mood (e.g., 'happy', 'sad', 'chill'): ")
        playlists = find_spotify_playlist(mood)
        if playlists:
            for i, playlist in enumerate(playlists):
                print(f"{i + 1}. {playlist['name']}")
                print(f"Link: {playlist['external_urls']['spotify']}")
                print()
            
            user_choice = int(input("Enter the number of the playlist you want to open: "))
            
            # Ensure the user input is valid
            if 1 <= user_choice <= len(playlists):
                selected_playlist = playlists[user_choice - 1]
                webbrowser.open(selected_playlist['external_urls']['spotify'])
                print(f"Opening playlist: {selected_playlist['name']}")
            else:
                print("Invalid choice. Please choose a valid number.")
        else:
            print("No playlists found for that mood.")

    elif user_input == 0: 
        print("Good Bye, Have a great day!") 
        break
    else: 
        print("Please enter valid user-input.") 
