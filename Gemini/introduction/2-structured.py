import os
from google import genai
from pydantic import BaseModel

from dotenv import load_dotenv 
# Load environment variables from a .env file
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25",
    contents="Pooran and Marsh  are going to the Art musuem on Saturday.",
    config={
        "response_mime_type": "application/json",
        "response_schema": CalendarEvent
    }
)

event = response.parsed
print(event.name, event.date, event.participants)
