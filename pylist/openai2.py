import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = 'https://docs-test-001.openai.azure.com/',
  api_key="linakey",
  api_version="2023-05-15"
)
completion = client.chat.completions.create(
    model="text-embedding-ada-002",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.model_dump_json(indent=2))