from groq import Groq

client = Groq(
    api_key="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"
)

def get_conversation_mood(conversation_text):
    """
    Asks the Groq API to determine the mood of a conversation based on the given text prompt.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Based on the following conversation, what mood or emotional tone is present? Give me a one word answer of a mood. Give me a one word color of the mood of the conversation after as well.  Conversation: '{conversation_text}'",
            }
        ],
        model="llama3-8b-8192",
    )
    
    # Retrieve and print the response
    mood_response = chat_completion.choices[0].message.content
    print("Conversation Mood:", mood_response)
    return mood_response

# Example usage
conversation_text = "I've had a bad week after I just failed my last Chemistry exam"
get_conversation_mood(conversation_text)
