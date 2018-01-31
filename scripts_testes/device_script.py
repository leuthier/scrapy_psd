import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiJjYzNjZTEwMC05ZmNlLTExZTYtODA4MC04MDgwODA4MDgwODAiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiY2JhNDRhODAtOWZjZS0xMWU2LTgwODAtODA4MDgwODA4MDgwIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNTE3NDAzNTE3LCJleHAiOjE1MTc0MDQ0MTd9.R71bPXe3ug8PldTN0a3Ir84eIrLdqYUaagBT963EFPrqf54pnu_fwvq8j01Bq2qsryNbyr9IIAfqT_ZhMpqJcA',
}

data = '{ \n   "additionalInfo": null, \n   "createdTime": 0, \n   "name": "teste de novo, de novo",\n   "type": "default" \n }'

response = requests.post('http://localhost:8080/api/device', headers=headers, data=data)

print(response.content)