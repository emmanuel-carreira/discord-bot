import os

from custom_client import CustomClient
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = CustomClient()
client.run(TOKEN)
