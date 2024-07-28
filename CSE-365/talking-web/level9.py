import requests as rq

response = rq.get("http://localhost:80/<path>")

print(response.text)
