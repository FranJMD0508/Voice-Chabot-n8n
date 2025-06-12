import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.environ.get("N8N_API_KEY")