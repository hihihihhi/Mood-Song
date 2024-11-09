import pvleopard
import sounddevice as sd
import numpy as np
import time
import keyboard
import spotify_part

# Initialize the Leopard API instance
access_key = "QBJxytrdXwNAfajs56uQE4GnjeYymGmYWwGCI4mDeQhH9eJ5tOD8GQ=="
handle = pvleopard.create(access_key)

# Set parameters for the audio recording
sample_rate = handle.sample_rate  # Ensure this matches `pvleopard` sample rate
chunk_length= 30  # seconds
spotifyObject = spotify_part.create_spotify_object()
'''def trigger_start_recording():
    """
    Checks if the song is within its last 30 seconds, triggering recording if true.
    """
    print("Checking for recording trigger based on Spotify playback...")
    
    if spotifyObject:
        remaining_time = spotify_part.get_remaining_time_in_song(spotifyObject)
        # Trigger recording if remaining time is between 30 and 35 seconds
        if remaining_time and 30 <= remaining_time <= 35:
            print("Trigger activated: Song is in the last 30 seconds.")
            return True
    
    print("Trigger not activated yet.")
    time.sleep(2)  # Check every 2 seconds to avoid excessive API calls
    return False'''

def trigger_start_recording(max_attempts=10, wait_time=2):
    """
    Checks if the song is within its last 30 seconds, triggering recording if true.
    Stops checking after `max_attempts` attempts.
    """
    print("Checking for recording trigger based on Spotify playback...")
    
    attempts = 0
    while attempts < max_attempts:
        if spotifyObject:
            remaining_time = spotify_part.get_remaining_time_in_song(spotifyObject)
            
            if remaining_time is not None:
                # Trigger recording if remaining time is between 30 and 35 seconds
                if 30 <= remaining_time <= 35:
                    print("Trigger activated: Song is in the last 30 seconds.")
                    return True
                else:
                    print(f"Song playing but not in last 30 seconds (Remaining time: {remaining_time}s).")
            else:
                print("No song currently playing.")
        else:
            print("Spotify object not initialized. Check if Spotify is authorized correctly.")
        
        # Wait before trying again and increase attempt counter
        time.sleep(wait_time)
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}...")

    print("Trigger not activated within maximum attempts.")
    return False

def record_chunk(chunk_length, sample_rate):
    #Records audio for a specified duration and returns as numpy array.
    print("Recording audio...")
    audio = sd.rec(int(chunk_length * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    return audio.flatten()

def transcribe_audio(audio_data):
    #Transciber function
    transcript, words = handle.process(audio_data)
    print("Transcript:", transcript)

# Main loop

'''try:
    while True:
        if trigger_start_recording():
            audio_data = record_chunk(chunk_length, sample_rate)
            transcribe_audio(audio_data)

except KeyboardInterrupt:
    print('Recording Stopped')'''

