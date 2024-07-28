import requests as rq

response = rq.get("http://localhost:80/?a=be25094b9a82a89e084b69fbdf23e731")

print(response.text)
