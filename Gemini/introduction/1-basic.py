import os
from google import genai
from dotenv import load_dotenv # type: ignore

load_dotenv()

# Initialize the Google GenAI client with your Gemini API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Generate a limerick using Gemini 2.5 Pro
response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25",
    contents=[
        "Write a limerick about the Python programming language."
    ]
)

print(response.text)