import os
import openai
import speech_utils as su


def main():
    language = ['en-IN', 'ta-IN']
    lang = language[0]

    
    print("Hello!!")
    su.text_to_speech(su.speech_to_text(0))


if __name__ == "__main__":
    os.system('cls')
    main()