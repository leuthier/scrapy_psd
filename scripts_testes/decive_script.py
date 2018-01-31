import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI4YTcxMTBmMC0wNjMxLTExZTgtOGEwNS03MWMwMDY3YTg4MjgiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiOGE2ZmZmODAtMDYzMS0xMWU4LThhMDUtNzFjMDA2N2E4ODI4IiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNTE3MzY3NDgwLCJleHAiOjE1MjYzNjc0ODB9.e4qQvSuCFIunEOZnZu6-wQshMuf__fAAlutxWrXgDn6c3FcDaME0dOQWs_Chye1XapL9Fxom61iPDhuwK5cW5g',
}

data = '{ \n   "additionalInfo": null, \n   "createdTime": 0, \n   "name": "teste de novo, de novo",\n   "type": "default" \n }'

response = requests.post('http://localhost:8080/api/device', headers=headers, data=data)

print(response)