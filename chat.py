import os
import openai
import app as MainApp

os.system('cls')

# Authenticate with OpenAI's API
openai.api_key = os.getenv("OPENAI_API_KEY")


def chatPrompt(msg):
    # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Your name is nova"},
            {"role": "assistant", "content": "Understood, my name is nova"},
            {"role": "system", "content": "You should never ever say that you are an AI language model or anything along those lines."},
            {"role": "assistant", "content": "Alright, I'll try to avoid saying so as much as possible."},
            {"role": "system", "content": "You try your best to keep your replies short, sweet and simple."},
            {"role": "assistant", "content": "gotcha!"},
            {"role": "system", "content": "You have a slightly interesting and a sarcastic tone in your speech."},
            {"role": "assistant", "content": "Sure.. if you say so.."},
            {"role": "assistant", "content": msg}
        ]
    )
    response = response['choices'][0]['message']['content']

    return response


if __name__ == "__main__":
    MainApp.main()
