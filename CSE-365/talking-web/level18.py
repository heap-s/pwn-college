import requests as rq

response = rq.get("http://localhost:80/?a=1e17eeeb870ad70d7977e6f5682afc61&b=1f3386a8+3c7d10b7%26c3f6d925%23f6cc6043")

print(response.text)
