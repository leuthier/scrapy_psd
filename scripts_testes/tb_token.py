import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

data = '{"username":"tenant@thingsboard.org", "password":"tenant"}'

response = requests.post('http://localhost:8080/api/auth/login', headers=headers, data=data)

print(response.content)