import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
from agent import room_client
from stt import transcribe_audio
from ai_response import generate_response
from tts import speak_response

load_dotenv()
app = Flask(__name__)

@app.route("/voice-response", methods=["POST"])
async def voice_response():
    response = VoiceResponse()
    
    # Connect to LiveKit (ensure room exists)
    room_client()
    
    # Process incoming audio (Twilio → AI)
    transcribed_text = await transcribe_audio(request.data)
    ai_response = await generate_response(transcribed_text)
    audio_response = await speak_response(ai_response)

    # Play AI response
    response.say(ai_response, voice="alice")
    
    return Response(str(response), mimetype="text/xml")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
