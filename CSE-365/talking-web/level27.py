import requests as rq
import json

d = {'a': 'value'}

headers = {"Content-Type": "application/json"}

response = rq.post('http://localhost:80', data=json.dumps(d), headers=headers)

print(response.text)
