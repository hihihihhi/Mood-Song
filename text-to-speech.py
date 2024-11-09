import pvleopard
import sounddevice as sd
import numpy as np
import time
import keyboard

# Initialize the Leopard API instance
access_key = "QBJxytrdXwNAfajs56uQE4GnjeYymGmYWwGCI4mDeQhH9eJ5tOD8GQ=="
handle = pvleopard.create(access_key)

# Set parameters for the audio recording
sample_rate = handle.sample_rate  # Ensure this matches `pvleopard` sample rate
chunk_length= 5  # seconds

def trigger_start_recording():
    #TODO implement a trigger for when a song is in it's last 30 seconds.  
    print("Waiting for trigger...")
    # Placeholder triggxser
    trigger = False
    # Wait for 2 seconds as a placeholder for actual trigger
    print("Triggered recording.")
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
'''
try:
    while True:
        if trigger_start_recording():
            audio_data = record_chunk(chunk_length, sample_rate)
            transcribe_audio(audio_data)

except KeyboardInterrupt:
    print('Recording Stopped')'''

