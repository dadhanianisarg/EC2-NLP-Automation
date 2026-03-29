from fastapi import FastAPI
from pydantic import BaseModel

from backend.nlp import parse_user_input
from backend.ec2_creator import create_ec2

app = FastAPI()


class Command(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "EC2 Automation Running 🚀"}


@app.post("/create")
def create(command: Command):
    config = parse_user_input(command.text)

    instance_id = create_ec2(config)

    return {
        "status": "success",
        "instance_id": instance_id,
        "config": config
    }