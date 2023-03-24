from msvcrt import getch
import os
import speech_utils as su
import chat


# def main():
try:
    while True:
        os.system('cls')
        print("Hello!!")
        user_input = su.speech_to_text(1)
        chat_output = chat.chatPrompt(user_input)
        su.text_to_speech(chat_output)

        print("\n\nPress 'q' to quit")
        if (getch() == 'q'):
            print("Bye!!")
            break
except KeyboardInterrupt:
    print("Quitting...")
