import urllib.request
import requests
import scrapy
from lxml import html

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
        url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php"
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"aleaNum\"\r\n\r\n4737\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"aleaValue\"\r\n\r\nNDczNw==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"dtaini\"\r\n\r\n10/01/2018\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"dtafim\"\r\n\r\n10/01/2018\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "0dd0e537-bbe6-e602-b7b4-a8be39d6014e"
            }
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        dados = response.xpath('normalize-space(//*[@id="FRM"]/table[3]/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[1])')
        print(dados)
##        eita = html.fromstring(response.content)
##        pegardados(eita)
##
##
        
def pegardados(url):
    dados = url.xpath('normalize-space(//*[@id="FRM"]/table[3]/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[1])')
    print ("dados",dados)
    
burlarcaptcha()

