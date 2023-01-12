import requests

print(requests.post('http://localhost:5000/execute/', json={
    "code": "print('Hello World')"
}).text)
