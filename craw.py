# -*- coding: utf-8 -*-

import dados_estacao
import requests
import urllib
import requests
import scrapy
import os
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
    lista_link = spider()
    
    url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"

    x = 1
    master_dic = {}
    for i in lista_link: #TODO: this can be a paramether

        print(" -----", x)
        x += 1
        print(" ----- CODIGO:",i)
        url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"+i+"=="

        form = {
                'dtaini':'17/01/2018', #TODO: get todays date using datetime
                'dtafim':'17/01/2018',
                'aleaValue':'NDgyOA==',
                'aleaNum':'4828'
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
            print(day_time_list)
            master_dic[i] = day_time_list
            # print(master_dic)
        else:
            print("nenhuma informação disponivel ou parametros de pesquisa invalidos")
    print(master_dic)




        

burlarcaptcha()

