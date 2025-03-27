import os
from livekit.plugins.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()
llm = OpenAIChat(api_key=os.getenv("openai_api_key"))

async def generate_response(transcribed_text):
    response = await llm.chat(transcribed_text)
    print("AI Response:", response)
    return response
