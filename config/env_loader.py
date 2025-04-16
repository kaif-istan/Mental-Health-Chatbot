# config/env_loader.py
from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "REDDIT_CLIENT_ID": os.getenv("REDDIT_CLIENT_ID"),
        "REDDIT_CLIENT_SECRET": os.getenv("REDDIT_CLIENT_SECRET"),
        "REDDIT_USER_AGENT": os.getenv("REDDIT_USER_AGENT")
    }
