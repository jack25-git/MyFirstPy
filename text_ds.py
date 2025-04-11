from http.client import responses

import requests

prompt=("请用小学生能听懂的语言解释为什么太阳会下山")

response= requests.post(
    url="http://127.0.0.1:11434/api/generate",
    json={
        "model":"deepseek-r1:1.5b",
        "prompt":prompt,
        "stream":False
    }
)
res=response.json()['response']
print(res)