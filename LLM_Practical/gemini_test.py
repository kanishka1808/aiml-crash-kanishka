from dotenv import load_dotenv
from google import genai
import os

print("Step 1: Loading .env")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Step 2: API Loaded")

client = genai.Client(api_key=api_key)

print("Step 3: Sending Request...")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Machine Learning?"
)

print("\nStep 4: Response Received\n")

print(response.text)