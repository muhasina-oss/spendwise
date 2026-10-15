
from google import genai

import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

#step1 : Authenticae

client = genai.Client(api_key=api_key)

prompt = "what is genai in simple words"

response = client.models.generate_content(
  
  model = "gemini-3.8-flash",
  contents = prompt
)

print(response.text)