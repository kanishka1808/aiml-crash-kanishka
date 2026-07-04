import os
from dotenv import load_dotenv
from groq import Groq

# Load API Key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Chat History
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("=" * 50)
print("AI Chat Assistant")
print("Type 'exit' to stop.")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Chat Ended.")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    print("\nAssistant: ", end="", flush=True)

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        stream=True
    )

    assistant_reply = ""

    for chunk in stream:

        content = chunk.choices[0].delta.content

        if content:

            print(content, end="", flush=True)

            assistant_reply += content

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )