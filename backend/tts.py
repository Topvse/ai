from gtts import gTTS

def synthesize_text(text: str, path: str):
    tts = gTTS(text=text, lang="ru")
    tts.save(path)

