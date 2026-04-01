from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os

from backend.nlp import parse_user_input
from backend.ec2_creator import create_ec2

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Command(BaseModel):
    text: str

# Serve frontend
@app.get("/")
def serve_ui():
    file_path = os.path.join(os.getcwd(), "frontend", "index.html")
    return FileResponse(file_path)

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# API
@app.post("/create")
def create(command: Command):
    config = parse_user_input(command.text)
    instance_id = create_ec2(config)

    return {
        "status": "success",
        "instance_id": instance_id,
        "config": config
    }