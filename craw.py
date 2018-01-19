# -*- coding: utf-8 -*-

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
    spider()
    
    url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"

    x = 1
    for i in lista_link:
        print(" -----",x)
        x += 1
        print(" ----- CODIGO:",i)
        url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"+i+"=="
            
        form = {
                'dtaini':'17/01/2018',
                'dtafim':'17/01/2018',
                'aleaValue':'NDgyOA==',
                'aleaNum':'4828'
                }
            
        encondedForm = urllib.parse.urlencode(form)

        head = {
                'Content-Type': 'application/x-www-form-urlencoded'
                }

        r = requests.post(url,data=encondedForm,headers=head)
        
##        pegardados(r)
            
            
##        dados = response.xpath('normalize-space(//*[@id="FRM"]/table[3]/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[1])')
##        print(dados)
##        eita = html.fromstring(response.content)
##        pegardados(eita)


        
def pegardados(response):
    print (" ----- RESPONSE CONTENT\n", response.text)
##    dados = url.xpath('normalize-space(//*[@id="FRM"]/table[3]/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[1])')
##    print ("dados",dados)
    
burlarcaptcha()

