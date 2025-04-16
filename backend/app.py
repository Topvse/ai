from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from tts import generate_speech
import os

app = FastAPI()

@app.get("/{file_name}")
async def get_audio_file(file_name: str):
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

@app.post("/say")
async def say(request: Request):
    data = await request.json()
    event = data.get("event", "unknown")
    element = data.get("element", "элемент")
    message = f"Вы нажали на {element}, событие: {event}"
    
    audio_file = generate_speech(message)
    
    return {"message": message, "audio_file": f"http://localhost:8000/{audio_file}"}

