import speech_utils as su

language = ['en-IN', 'ta-IN']
lang = language[0]
api=["google", "whisper", "sphinx"]

print("Hello!!")
su.text_to_speech(su.speech_to_text(api[0]))
