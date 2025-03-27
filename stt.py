import os
from livekit.plugins.deepgram import DeepgramSTT
from dotenv import load_dotenv
#basic code without logging
load_dotenv()
stt = DeepgramSTT(api_key=os.getenv("deepgram_api_key"))

async def transcribe_audio(audio):
    text = await stt.transcribe(audio)
    print("Transcribed:", text)
    return text
