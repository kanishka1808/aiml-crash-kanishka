from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(query, retrieved_docs, chat_history):

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    history = ""

    if chat_history:
        history = "\nPrevious Conversation:\n"

        for chat in chat_history[-5:]:
            history += f"User: {chat['question']}\n"
            history += f"Assistant: {chat['answer']}\n\n"

    prompt = f"""
You are AuraHealth Nexus AI Assistant.

You MUST follow these rules:

1. Answer ONLY using the provided context.
2. Never use outside knowledge.
3. Use previous conversation if it helps answer follow-up questions.
4. If the answer is not available in the context, reply exactly:
"I don't know based on the provided documents."
5. Keep answers clear and concise.
6. Mention exact values, names, codes, percentages, room numbers, dosages, or timings whenever available.

{history}

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()