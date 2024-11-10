Readme

Mood-Song: Real-Time Mood-Based Playlist Generator
Mood-Song is an application that listens to conversations, analyzes mood based on the transcription, and triggers mood-matching playlists from Spotify. It also provides an immersive lighting experience by syncing a NeoPixel LED matrix to the detected mood.

Features:
Real-Time Speech-to-Text: Uses pvleopard for continuous speech transcription.
Mood Detection: Groq API analyzes conversation transcripts to determine mood.
Spotify Playlist Integration: Plays Spotify playlists that align with the detected mood.
Mood-Based LED Matrix: NeoPixel LED matrix changes colors to match mood and pulse to music energy.

Installation:
Prerequisites
Python 3.x
Raspberry Pi 3 with a 16x16 NeoPixel LED matrix
Spotify Developer account credentials for API access
Setup Instructions
Clone the repository:
git clone https://github.com/yourusername/mood-song.git

Install dependencies:
pip install pvleopard spotipy sounddevice neopixel

Set up Spotify API credentials:

Create a .env file with your Spotify client ID, client secret, and redirect URI.
Set up API Keys:

Add your Groq and pvleopard API keys in the script where indicated.

Project Structure:
├── mood_song.py                # Main app script
├── spotify_part.py             # Spotify integration functions
├── speech_to_text.py           # Functions for recording and transcribing audio
├── neoPixel.py                 # NeoPixel LED matrix control
└── README.md                   # Project documentation

Configuration
Spotify Configuration
The spotify_part.py module contains functions for managing Spotify playback, retrieving song details, and playing mood-matching playlists.

NeoPixel Configuration
The neoPixel.py script contains functions for controlling a NeoPixel LED matrix based on mood color.

API Documentation
Leopard API: Transcribes speech in real-time.
Groq API: Analyzes conversation transcripts to detect mood.
Spotify API: Fetches playlists and controls playback based on mood.
Troubleshooting
No Active Device Error: Ensure Spotify is open and active on a device.
NeoPixel Issues: Ensure the LED matrix is properly connected to your Raspberry Pi.
