import pvleopard
import sounddevice as sd
import time
import spotify_part

# Initialize the Leopard API instance
access_key = "QBJxytrdXwNAfajs56uQE4GnjeYymGmYWwGCI4mDeQhH9eJ5tOD8GQ=="
handle = pvleopard.create(access_key)

# Set parameters for the audio recording
sample_rate = handle.sample_rate  # Ensure this matches `pvleopard` sample rate
chunk_length= 30  # seconds
spotifyObject = spotify_part.create_spotify_object()

def trigger_start_recording(max_attempts=10, wait_time=2):
    """
    Checks if the song is within its last 30 seconds, triggering recording if true.
    Stops checking after `max_attempts` attempts.
    """
    print("Checking for recording trigger based on Spotify playback...")
    
    attempts = 0
    duration = spotify_part.get_duration(spotifyObject)

    while True:
        time.sleep(2)
        
        if spotifyObject:
            current_time = spotify_part.get_time(spotifyObject)
            #print(current_time)
            if (duration-current_time)/1000 < 35:
                return True
            
            #    return True 
        else:
            return False
    
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
    return transcript



