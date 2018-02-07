import requests
import time

def publish(hora, temp_max, temp_min, temp_inst, pressao, radiacao, vento_vel, vento_rajada, data, latitude):
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI4YTcxMTBmMC0wNjMxLTExZTgtOGEwNS03MWMwMDY3YTg4MjgiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiOGE2ZmZmODAtMDYzMS0xMWU4LThhMDUtNzFjMDA2N2E4ODI4IiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNTE3OTMzNDY1LCJleHAiOjE1MjY5MzM0NjV9.K-weRFt0sDr-xVbhG0Ll7LV9LDpP8w-oWoXnjjRtXEXmvibL-zUcS1g54QEjuf8AjpmGcj1ncHkOQQDkHANMLw',
    }
    data = '{ \n   "hora": "' + str(hora) + '", \n   "temp_max": ' + str(temp_max) + '", \n   "temp_min": "' + str(temp_min) + '", \n   "temp_inst": "' + str(temp_inst) + '", \n   "pressao": ' + str(pressao) + '", \n   "radiacao": "' + str(radiacao) + '", \n    "vento_vel": "' + str(vento_vel) + '", \n   "vento_rajada": ' + str(vento_rajada) + '", \n   "data": "' + str(data) + '", \n   "latitude": "' + str(latitude) + '", \n }'

    response = requests.post('http://localhost:8080/api/v1/xhYxUqcyRiEitxGBAofl/atributes', headers=headers, data=data)
    print(response.content)


def get_telemetry():

    headers = {
        'Content-Type': 'application/json',
        'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI4YTcxMTBmMC0wNjMxLTExZTgtOGEwNS03MWMwMDY3YTg4MjgiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiOGE2ZmZmODAtMDYzMS0xMWU4LThhMDUtNzFjMDA2N2E4ODI4IiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNTE3OTMzNDY1LCJleHAiOjE1MjY5MzM0NjV9.K-weRFt0sDr-xVbhG0Ll7LV9LDpP8w-oWoXnjjRtXEXmvibL-zUcS1g54QEjuf8AjpmGcj1ncHkOQQDkHANMLw',
    }

    params = (
        ('keys', 'temperatura,velocidade,ligado'),
        ('startTs', ''),
        ('endTs', ''),
        ('interval', ''),
        ('limit', ''),
        ('agg', ''),
    )

    response = requests.get(
        'http://localhost:8080/api/plugins/telemetry/DEVICE/5445f210-08d0-11e8-9bfd-71c0067a8828/values/timeseries',
        headers=headers, params=params)

#     método antigo de request, sem passagem dos parâmetros, para teste direto no URL
#     response = requests.get('http://localhost:8080/api/plugins/telemetry/DEVICE/ac8e6020-ae99-11e6-b9bd-2b15845ada4e/values/timeseries?keys=gas,temperature', headers=headers)
    print(response.content)
    return response.content


# teste do publish
i = 0
t = 300
v = 400
# for i in range(100):
#    if i % 2 == 0:
#        li = "true"
#    else:
#        li = 'false'
publish(00, -22.7, -23.2, -23.1, 841, 1000, 7, 8, '07/02/2018', -84.0000)
#    time.sleep(2)
#    t += 5
#    v -= 1
#    i += 1
