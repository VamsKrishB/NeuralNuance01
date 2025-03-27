import os
from livekit.plugins.elevenlabs import ElevenLabsTTS
from dotenv import load_dotenv
#basic TTS integration
load_dotenv()
tts = ElevenLabsTTS(api_key=os.getenv("elevenlabs_api_key"))

async def speak_response(text):
    audio = await tts.synthesize(text)
    return audio
