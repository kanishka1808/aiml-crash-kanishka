from dotenv import load_dotenv
from groq import Groq
import os

print("Step 1: Loading .env")

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("Step 2: API Loaded")
print("Groq Key:", api_key[:10], "...")

client = Groq(api_key=api_key)

print("Step 3: Sending Request...")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "What is Machine Learning?"
        }
    ]
)

print("\nStep 4: Response Received\n")

print(response.choices[0].message.content)