# HOW TO USE OPENAI IN PYTHON

from openai import OpenAI

OPEN_AI_KEY = ""

selected_model ='gpt-4o-mini'
client = OpenAI(api_key=OPEN_AI_KEY)

response = client.responses.create(
    model=selected_model,
    input="Write a job description for an agentic ai role in 2025"
)

print(response.output_text)