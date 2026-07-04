import os
import pandas as pd
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Same use case (Summarization)
text = """
Artificial Intelligence is transforming healthcare by helping doctors diagnose diseases,
analyzing medical images, predicting patient risks, improving treatment planning,
and assisting in drug discovery. AI helps hospitals improve efficiency and patient care.
"""

# Five Different Prompts
prompts = [
    "Summarize the text.",
    "Summarize the text in exactly 50 words.",
    "Summarize the text using bullet points.",
    "Explain the text for a 10-year-old child.",
    "Extract only the important keywords from the text."
]

results = []

for i, prompt in enumerate(prompts, start=1):

    full_prompt = prompt + "\n\n" + text

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=full_prompt
    )

    results.append({
        "Prompt No": i,
        "Prompt": prompt,
        "Output": response.text
    })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("prompt_outputs.csv", index=False)

print("\n========== TASK 2 OUTPUT ==========\n")

print(df)

print("\nCSV File Saved Successfully!")