import time
import sounddevice as sd
import pvleopard
import spotify_part
import textToGPT
import speech_to_text
from groq import Groq
import numpy as np

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
    print("Starting to record...")
    audio_data = speech_to_text.record_chunk(chunk_length, sample_rate)  # Record for 30 seconds
    transcript = speech_to_text.transcribe_audio(audio_data)  # Transcribe the recorded audio
    mood_response = textToGPT.get_conversation_mood(transcript)
    print("Detected Mood: ", mood_response)
    spotify_part.play_playlist_by_mood(mood_response)

if __name__ == "__main__":
    main()
