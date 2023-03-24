import os
import openai


# Authenticate with OpenAI's API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your prompt
prompt = "Hello"

# Set up the parameters for the OpenAI API request
model_engine = "text-davinci-002"
temperature = 0.7
max_tokens = 100

# Use the OpenAI API to generate a response to your prompt
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Print the response text
print(response.choices[0].text.strip())