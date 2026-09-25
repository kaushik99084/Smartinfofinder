import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-20b"
MAX_TOKENS = 1024

TEMPERATURE = 0.7

APP_NAME = "Smart Info Finder"
APP_ICON = "🔍"