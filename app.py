from msvcrt import getch
import os
import speech_utils as su
import chat


def main():
    language = ['en-IN', 'ta-IN']
    lang = language[0]

    
    print("Hello!!")
    su.text_to_speech(chat.chatPrompt(su.speech_to_text()))


if __name__ == "__main__":
    while True:
        os.system('cls')
        main()
        if (getch() == 'q'):
            break
