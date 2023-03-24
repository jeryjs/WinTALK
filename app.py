from msvcrt import getch
import os
import speech_utils as su
import chat


def main():
    print("Hello!!")
    input = su.speech_to_text(0)
    chat_output = chat.chatPrompt(input)
    su.text_to_speech(chat_output)


if __name__ == "__main__":
    try:
        while True:
            os.system('cls')
            main()
            print("\n\nPress 'q' to quit")
            if (getch() == 'q'):
                print("Bye!!")
                break
    except KeyboardInterrupt:
        print("Quitting...")
