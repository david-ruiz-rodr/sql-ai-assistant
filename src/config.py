import os
from dotenv import load_dotenv

load_dotenv()  # lee .env en el root

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/sample.db")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

