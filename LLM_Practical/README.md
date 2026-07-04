# LLM Practical Assignment

## Student Details

Name: Kanishka

## Overview

This project demonstrates the use of Large Language Models (LLMs) using Gemini and Groq APIs.

## Tasks Completed

### Task 1: Multi-LLM Comparison
- Compared Gemini and Groq responses
- Measured response time
- Measured response length
- Saved results in responses.csv

### Task 2: Prompt Engineering
- Tested 5 different prompts
- Compared outputs
- Saved results in prompt_outputs.csv

### Task 3: Streaming AI Chat Assistant
- Built a chatbot using Groq API
- Implemented chat history
- Implemented streaming responses

### Task 4: Token Usage and Cost Tracker
- Recorded prompt and response
- Calculated token usage
- Estimated API cost
- Saved report in usage_report.csv

## Technologies Used

- Python
- Google Gemini API
- Groq API
- Pandas
- Python Dotenv

## How to Run

1. Create virtual environment
2. Install dependencies

pip install -r requirements.txt

3. Add API keys in .env

GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key

4. Run any task

python task1.py
python task2.py
python task3.py
python task4.py