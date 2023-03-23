import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

language = ['en-IN', 'ta-IN']
lang = language[0]
model=["google", "whisper", "sphinx"]

    
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
            stt_output = r.recognize_whisper(audio, model='tiny')
        elif model == "sphinx":
            stt_output = r.recognize_sphinx(audio)
            
        print('Converting audio transcripts into text\n\n「'+ stt_output+'」\n')
    except Exception as e:
        stt_output="Sorry, I didnt get that.."
        print("\n"+stt_output+"\n", e)

    return stt_output



def text_to_speech(text):
    print('tts-ing...')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()
