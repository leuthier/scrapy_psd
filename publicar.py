from .device_config import *


def publish(hora, temp_max, temp_min, temp_inst, pressao, radiacao, vento_vel, vento_rajada, data, latitude):
    token = 'Bearer ' + get_token_sys()
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'X-Authorization': token
    }
    # formato correto dos dados passados
    data = '{ \n   "hora": "' + str(hora) + '", \n   "temp_max": ' + str(temp_max) + '", \n   "temp_min": "' + str(temp_min) + '", \n   "temp_inst": "' + str(temp_inst) + '", \n   "pressao": ' + str(pressao) + '", \n   "radiacao": "' + str(radiacao) + '", \n    "vento_vel": "' + str(vento_vel) + '", \n   "vento_rajada": ' + str(vento_rajada) + '", \n   "data": "' + str(data) + '", \n   "latitude": "' + str(latitude) + '", \n }'

    response = requests.post('http://localhost:8080/api/v1/xhYxUqcyRiEitxGBAofl/telemetry', headers=headers, data=data)
    print(response.content)

# retorno dos dados por telimetria,
def get_telemetry():
    token = 'Bearer ' + get_token_sys()
    headers = {
        'Content-Type': 'application/json',
        'X-Authorization': token,
    }

    # parametros nao aceitos corretamente, 503, Bad request, nao foi encontrado um padrao para teste para as variaveis
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
publish(00, -22.7, -23.2, -23.1, 841, 1000, 7, 8, '07/02/2018', -84.0000)
