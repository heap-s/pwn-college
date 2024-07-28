import requests as rq

d = {'a': '86c32abe1dd60e1f7c4be779074415dd'}

response = rq.post('http://localhost:80', data=d) 

print(response.text)
