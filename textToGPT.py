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
                "content": f"Based on the following conversation, what genre? Give me a one word answer of a genre. Reply one word and one word only. Conversation: '{conversation_text}'",
            }
        ],
        model="llama3-8b-8192",
    )
    
    # Retrieve and print the response
    
    mood_response = chat_completion.choices[0].message.content
    print("Conversation Mood:", mood_response)
    return mood_response


def get_mood_color(mood_response):
    """
    Asks the Groq API to determine the mood of a conversation based on the given text prompt.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Based on the following word, give me a color RGB tuple that cooresponds to the word.  Only give me the tuple in a comma seperated list with no parentheses,no spaces, no other output:{mood_response}"
            }
        ],
        model="llama3-8b-8192",
    )
    
    # Retrieve and print the response
    
    mood_color = chat_completion.choices[0].message.content
    print("Mood Color:", mood_color)
    mood_color = tuple(map(int, mood_color.split(",")))
    return mood_color


