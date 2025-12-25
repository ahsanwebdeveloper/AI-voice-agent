import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  

def text_to_speech(text, output_file="response.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    
    with open(output_file, "wb") as f:
        f.write(response.content)

    return output_file
