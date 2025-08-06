# HOW TO USE OPENAI IN PYTHON

from openai import OpenAI

OPEN_AI_KEY = "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"

selected_model ='gpt-4o-mini'

client = OpenAI(api_key=OPEN_AI_KEY)

response = client.responses.create(
    model=selected_model,
    input="Write a job description for an agentic ai role in 2025"
)

response.text