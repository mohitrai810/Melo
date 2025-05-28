from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import uuid
from app.utils import synthesize

app = FastAPI()

@app.post("/speak")
def speak(text: str = Form(...)):
    output_path = f"/tmp/{uuid.uuid4().hex}.wav"
    synthesize(text, output_path)
    return FileResponse(output_path, media_type="audio/wav", filename="output.wav")
