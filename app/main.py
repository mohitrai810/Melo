from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
from TTS.api import TTS
import uuid
import os

app = FastAPI()

# Load TTS model once on startup
tts = TTS(model_name="tts_models/multilingual/multi-dataset", progress_bar=False)

@app.post("/speak")
async def speak(text: str = Form(...)):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    output_path = f"/tmp/{uuid.uuid4()}.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    
    return FileResponse(output_path, media_type="audio/wav", filename="output.wav")
