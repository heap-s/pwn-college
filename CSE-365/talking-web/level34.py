import requests as rq

response = rq.get('http://localhost:80', allow_redirects=True)

print(response.text)
