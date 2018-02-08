import requests
from dados_estacao import pegarestacoes


def get_token_sys():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    data = '{"username":"tenant@thingsboard.org", "password":"tenant"}'

    response = requests.post('http://localhost:8080/api/auth/login', headers=headers, data=data)

    t = str(response.content)
    t = t.split('"')
    token = str(t[3])
    return token


def create_device(name):
    token = 'Bearer ' + get_token_sys()
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Authorization': token,
    }

    data = '{ \n   "additionalInfo": null, \n   "createdTime": 0, \n   "name": "' + str(
        name) + '",\n   "type": "default" \n }'

    response = requests.post('http://localhost:8080/api/device', headers=headers, data=data)

    t = str(response.content)
    t = t.split('"')
    device_id = t[9]
    device_name = t[-8]

    g = open("devices.txt", "a")
    g.write(device_name + "\n")
    g.write(device_id + "\n")
    g.close()
    print(device_id)
    print(data)
    print(response.content)
    return str(device_id)


# file = open("devices.txt", "r")
# ls = file.readlines()
# local = ls[1]
# local = local.split(" ")
# local = local[2].split("\n")
# device_id = str(local[0])


def get_credentials(device):
    token = 'Bearer ' + get_token_sys()
    headers = {
        'Accept': 'application/json',
        'X-Authorization': token,
    }

    response = requests.get('http://localhost:8080/api/device/' + str(device) + '/credentials', headers=headers)
    t = str(response.content)
    t = t.split('"')
    print(t)
    credential = str(t[-4])
    g = open("credentials.txt", "a")
    g.write(credential + "\n")
    g.close
    return credential


# arquivo antigo para pegar o id do arquivo, com os nomes dos devices e seus ids, método reformulado

# file = open("devices.txt", "r")
# ls = file.readlines()
# local = ls[1]
# local = local.split(" ")
# local = local[2].split("\n")
# device_id = str(local[0])

# create_device(nome)


dic = pegarestacoes()
print(dic.keys())
first = list(dic.keys())
first = first[0]
dev = create_device(first)
cred = get_credentials(dev)
print(cred)
