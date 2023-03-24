import openai
import speech_utils as su


def main():
    language = ['en-IN', 'ta-IN']
    lang = language[0]
    api = ["google", "whisper", "sphinx"]

    
    print("Hello!!")
    su.text_to_speech(su.speech_to_text(api[1]))


if __name__ == "__main__":
    main()
    # audio = open("temp.wav", "rb")
    # output = openai.Audio.transcribe('whisper-1', audio)
    # print(output)