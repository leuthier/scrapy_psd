import urllib.request
import requests

lista_link = []

def spider():

    i = 0

    content = urllib.request.urlopen("http://www.inmet.gov.br/sonabra/maps/pg_mapa.php").read()
    content = str(content)

    while i < len(content):
        find = 'http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?'
        i = content.find(find, i)
        if i == -1:
            break
        else:
            posicao = int(i + len(find))
            teste = content[posicao: posicao + 6]
            lista_link.append(teste)
            i += len(find)
    return lista_link


def burlarcaptcha():
    spider()
    url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php"
    x = 1
    for i in lista_link:
        print(x)
        x += 1
        print(i)
        querystring = {i: "="}
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"aleaNum\"\r\n\r\n0917\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"geraImg.php?imgNum=MDkxNw==\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
               'cache-control': "no-cache", 'postman-token': "eb6b86b9-da6a-30c5-99ad-8a9b58fc6a5c"}
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        print(response.text)



burlarcaptcha()

