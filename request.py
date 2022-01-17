import requests

url = 'http://0.0.0.0:8000/user'

data = {
    'name': 'Maria',
    'email': 'maria.silva@gmail.com',
    'password': '45678',
    'role_id': 2
}

request = requests.post(url=url, json=data)
print(request.json())
