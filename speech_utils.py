import io
import os
import app as MainApp
from time import sleep
import openai
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

language = ['en-IN', 'ta-IN']
lang = language[0]
model = ["google", "whisper", "sphinx"]
openai.api_key = os.getenv("OPENAI_API_KEY")


def speech_to_text(model=model[0]):
    r = sr.Recognizer()

    # with sr.AudioFile("Recording.wav") as source:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("processing request")

    stt_output = ""
    try:
        if model == "google":
            stt_output = r.recognize_google(audio)

        elif model == "whisper":
            # save audio as WAV file
            with open("temp.wav", "wb") as f:
                f.write(audio.get_wav_data())
            with open("temp.wav", "rb") as audio:
                stt_output = openai.Audio.transcribe('whisper-1', audio)
                stt_output = stt_output['text']
            os.remove("temp.wav")

        elif model == "sphinx":
            stt_output = r.recognize_sphinx(audio)

        print('Converting audio transcripts into text\n\n「' + stt_output+'」\n')
    except Exception as e:
        stt_output = "Sorry, I didnt get that.."
        print("\n"+stt_output+"\n", e)

    return stt_output


def text_to_speech(text):
    print('tts-ing...')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    MainApp.main()
