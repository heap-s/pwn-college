import requests

headers = {"Host": "e7e2e02506af6ffa86e34c521d6666bd"}

response = requests.get("http://127.0.0.1:80", headers=headers)

print(response.text)
