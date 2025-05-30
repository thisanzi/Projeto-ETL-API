import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type":"application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages":[{"role": "user", "content": "Qual é a capital da França?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())