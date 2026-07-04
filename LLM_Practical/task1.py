import os
import time
import pandas as pd

from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

# -------------------------------
# API Keys
# -------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------------
# Clients
# -------------------------------

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

groq_client = Groq(api_key=GROQ_API_KEY)


# -------------------------------
# Gemini Function
# -------------------------------

def get_gemini_response(prompt):

    start = time.time()

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    end = time.time()

    return {
        "Provider": "Gemini",
        "Response": response.text,
        "Time": round(end-start,2),
        "Length": len(response.text)
    }


# -------------------------------
# Groq Function
# -------------------------------

def get_groq_response(prompt):

    start = time.time()

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    text = response.choices[0].message.content

    end = time.time()

    return {
        "Provider":"Groq",
        "Response":text,
        "Time":round(end-start,2),
        "Length":len(text)
    }


# -------------------------------
# Main Program
# -------------------------------

prompt=input("Enter your Prompt : ")

gemini=get_gemini_response(prompt)

groq=get_groq_response(prompt)

data=[gemini,groq]

df=pd.DataFrame(data)

print("\nComparison Table\n")
print(df)

df.to_csv("responses.csv",index=False)

print("\nresponses.csv saved successfully.")