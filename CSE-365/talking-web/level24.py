import requests as rq

d = {'a': '118eee943586c4607058076e7faa35a8', 'b': 'dd1f4f6d 92b360bd&231fedc2#7b6e620f'}

response = rq.post('http://localhost:80', data=d) 

print(response.text)
