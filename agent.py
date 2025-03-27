import os
import livekit
from livekit import api

from dotenv import load_dotenv

load_dotenv()

livekit_url = os.getenv("livekit_url")
livekit_api_key = os.getenv("livekit_api_key")
livekit_api_secret = os.getenv("livekit_api_secret")


if __name__ == "__main__":
    try:
        room_client = livekit.RoomServiceClient(livekit_url, livekit_api_key, livekit_api_secret)

        room = room_client.create_room(livekit.CreateRoomRequest(name="BFSI_Voice_Agent"))

        print(f"Room Created: {room.name}")

    except Exception as e:
        print(f"An error occurred: {e}")
