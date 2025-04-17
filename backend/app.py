from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from uuid import uuid4
from tts import synthesize_text
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
os.makedirs("audio", exist_ok=True)
app.mount("/static", StaticFiles(directory="audio"), name="static")

@app.post("/say")
async def say(request: Request):
    body = await request.json()
    event = body.get("event")
    element = body.get("element")

    if not event or not element:
        return JSONResponse(content={"error": "Invalid input"}, status_code=400)

    message = f"Вы нажали на {element}, событие: {event}"
    filename = f"output_{uuid4()}.mp3"
    filepath = f"audio/{filename}"
    synthesize_text(message, filepath)

    return {
        "message": message,
        "audio_file": f"/static/{filename}"
    }

