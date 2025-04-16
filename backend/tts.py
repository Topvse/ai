from gtts import gTTS

def generate_speech(text: str, filename: str = "output.mp3"):
    tts = gTTS(text=text, lang="ru")
    tts.save(filename)
    return filename

