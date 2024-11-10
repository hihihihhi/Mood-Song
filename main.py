from time import sleep
from spotify_part import play_playlist_by_mood
from textToGPT import get_conversation_mood
import speech_to_text


# Set parameters for the audio recording
chunk_length = 5  # seconds (for the 30-second chunk)

# Initialize the Groq API instance for mood analysis


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
                mood_response = get_conversation_mood(transcript)
                print("Detected Mood:", mood_response)

                # Play playlist based on detected mood
                play_playlist_by_mood(mood_response)

                # Pause before checking for the next trigger
                sleep(5)  # Wait a bit to prevent immediate retriggering
                a=speech_to_text.trigger_start_recording()
    except KeyboardInterrupt:
        print("Mood-Song app stopped.")

# Loop the main function continuously
if __name__ == "__main__":
    main()
