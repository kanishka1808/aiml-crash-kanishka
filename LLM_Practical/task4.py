import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Estimated Cost
# (Example: $0.59 per 1M input tokens and $0.79 per 1M output tokens)
INPUT_COST = 0.59 / 1000000
OUTPUT_COST = 0.79 / 1000000

logs = []

while True:

    prompt = input("Enter Prompt (type exit to stop): ")

    if prompt.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens

    cost = (prompt_tokens * INPUT_COST) + \
           (completion_tokens * OUTPUT_COST)

    logs.append({
        "Prompt": prompt,
        "Response": answer,
        "Prompt Tokens": prompt_tokens,
        "Completion Tokens": completion_tokens,
        "Total Tokens": total_tokens,
        "Estimated Cost ($)": round(cost, 8)
    })

df = pd.DataFrame(logs)

df.to_csv("usage_report.csv", index=False)

print("\n========== FINAL REPORT ==========\n")

print(df)

print("\nTotal Requests :", len(df))
print("Total Tokens :", df["Total Tokens"].sum())
print("Estimated Cost ($):", round(df["Estimated Cost ($)"].sum(),8))

print("\nusage_report.csv saved successfully.")