import openai
from openai_secret_manager import get_secret

secrets = get_secret("openai")

openai.api_key = secrets["org-nOUEzLBTCgkwrpoMs9hh64z6"]

prompt = "Hello, what can you do?"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=60
)

print(response.choices[0].text)