import time
import sounddevice as sd
import pvleopard
import spotify_part
import textToGPT
import speech_to_text
from groq import Groq
from spotify_part import *

# Initialize the Leopard API instance
access_key = "QBJxytrdXwNAfajs56uQE4GnjeYymGmYWwGCI4mDeQhH9eJ5tOD8GQ=="
handle = pvleopard.create(access_key)

# Set parameters for the audio recording
sample_rate = handle.sample_rate  # Ensure this matches `pvleopard` sample rate
chunk_length = 30  # seconds (for the 30-second chunk)

# Initialize the Groq API instance for mood analysis
groq_client = Groq(
    api_key="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"
)

def main():
    print("Starting Mood-Song app...")
    a = True
    try:
        while True:
            # Check for recording trigger based on Spotify playback
            if a:
                print("Recording started...")

                # Record a 30-second audio chunk
                audio_data = speech_to_text.record_chunk(chunk_length, speech_to_text.sample_rate)

                # Transcribe the recorded audio
                transcript = speech_to_text.transcribe_audio(audio_data)

                # Analyze the transcript to detect mood
                mood_response = textToGPT.get_conversation_mood(transcript)
                print("Detected Mood:", mood_response)

                # Play playlist based on detected mood
                spotify_part.play_playlist_by_mood(mood_response)

                # Pause before checking for the next trigger
                time.sleep(5)  # Wait a bit to prevent immediate retriggering
                a=speech_to_text.trigger_start_recording()
    except KeyboardInterrupt:
        print("Mood-Song app stopped.")

# Loop the main function continuously
if __name__ == "__main__":
    main()
