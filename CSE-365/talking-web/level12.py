import requests as rq

response = rq.get("http://localhost:80/9bbb2690%201f187680/887553d4%20f2a811cd")

print(response.text)
