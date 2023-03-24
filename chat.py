import os
import openai

os.system('cls')

# Authenticate with OpenAI's API
openai.api_key = os.getenv("OPENAI_API_KEY")


def chatPrompt(msg):
    # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    response = response['choices'][0]['message']['content']

    return response