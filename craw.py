# -*- coding: utf-8 -*-

from dados_estacao import pegarestacoes
import urllib
import requests
from datetime import datetime

list_link = []


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
            list_link.append(teste)
            i += len(find)
    return list_link


def try_captcha():
    lista_link = spider()

    now = datetime.now()
    today = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    # print(today)
    x = 1
    master_dic = {}
    # for i in lista_link:
    i = lista_link[0]
    # print(" -----", x)
    x += 1
    # print(" ----- CODIGO:", i)
    url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?" + i + "=="

    form = {
        'dtaini': today,
        'dtafim': today,
        'aleaValue': 'NDgyOA==',
        'aleaNum': '4828'
    }

    encondedForm = urllib.parse.urlencode(form)

    head = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(url, data=encondedForm, headers=head)
    cook = r.cookies.items()
    cookies = "{}={}".format(cook[0][0], cook[0][1])
    # print(cookies)

    head2 = {
        'Referer': url,
        'Cookie': cookies
    }

    n = requests.get("http://www.inmet.gov.br/sonabra/pg_downDadosCodigo_sim.php", headers=head2)
    day_time_list = []
    data_time = {}
    response = n.text
    response = response.replace('////', "-")
    response = response.replace("\r\n\t\t", "")
    response = response.replace("\r\n", "")
    response = response.replace(" ", "")
    response = response.split("<br>")
    response = response[:-1:]
    # for x in response: print(x, len(x.split(",")))
    if len(response) > 0:

        categories = response.pop(0).split(",")
        for data_set in response:
            for data_index in range(len(data_set.split(","))):
                data_time[categories[data_index]] = data_set.split(",")[data_index]
            day_time_list.append(data_time)

        # valores horarios de uma medicao coletada
        hora = day_time_list[0]['hora']
        temp_min = day_time_list[0]['temp_min']
        temp_max = day_time_list[0]['temp_max']
        temp_inst = day_time_list[0]['temp_inst']
        pressao = day_time_list[0]['pressao']
        radiacao = day_time_list[0]['radiacao']
        vento_vel = day_time_list[0]['vento_direcao']
        vento_rajada = day_time_list[0]['vento_rajada']
        data = day_time_list[0]['data']
        # print(hora, temp_max, temp_min, temp_inst, pressao, radiacao, vento_vel, vento_rajada, data, latitude)
        master_dic[i] = day_time_list

        # dicionario principal com todos os dados coletados de todas as estacoes com valores do dia
        # print(master_dic)
    else:
        print("nenhuma informação disponivel ou parametros de pesquisa invalidos")

    return day_time_list


try_captcha()
