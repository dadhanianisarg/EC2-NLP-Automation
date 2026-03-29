import os
from dotenv import load_dotenv
from pathlib import Path

# ✅ Get absolute path to .env
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION") or "ap-south-1"

print("CONFIG LOADED")
print("KEY:", AWS_ACCESS_KEY)
print("REGION:", AWS_REGION)