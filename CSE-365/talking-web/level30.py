import requests as rq
import json 

d = {'a': 'de6ec7747dd993aa6e34742515b45a8f', 'b': {'c': 'f9356530', 'd': ['03800e24', '0c5a6a45 1a19d89a&c7156917#98b1eb34']}}

headers = {"Content-Type": "application/json"}

response = rq.post('https://localhost:80', data=json.dumps(d), headers=headers)

print(response.text)
