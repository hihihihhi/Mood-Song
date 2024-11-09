import openai
import time

openai.api_key = "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"

text = "It's pretty decent. It'll definitely be enough for what we need to do. We'll make it ball."

# Function to make API call with rate limiting
def get_response():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Given the following conversation return a genre, mood, or category that would make sense in the context of music:" + text}]
        )
        print(response['choices'][0]['message']['content'])
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Waiting for 5 seconds before retrying...")
        time.sleep(5)  # Wait for 10 seconds before retrying
        get_response()  # Retry the request

# Call the function to get the response
get_response()
