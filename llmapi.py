import requests
import json
import os


def get_response(messages: list[dict]) -> str:
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.environ.get('AI_TOKEN')}"
    },
    data=json.dumps({
        "model": "openai/gpt-4o-mini", # Optional
        "messages": messages
    })
    )

    return response.json()['choices'][0]['message']['content']