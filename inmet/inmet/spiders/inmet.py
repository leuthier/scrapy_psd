# -*- coding: utf-8 -*-
try:
    import urllib.request
    import requests
    import scrapy
    import os

    from scrapy.http import FormRequest
    from scrapy.utils.response import open_in_browser
    from lxml import html
    
except:
    print ("Erro ao importar algum dos pacotes necessarios")
    os.system('cls')
    print ("Aguarde a instalacao :)")
    try:
        os.system('pip install -r requirements.txt')
    except:
        print ("Houve um erro durante a instalacao de algum dos pacotes necessarios")

class ExampleSpider(scrapy.Spider):
    name = 'inmet'
    allowed_domains = ['inmet.gov.br']
    start_urls = ['http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?QTEwOA==']
    lista_link = []
    
    def pegarcodigos(self):
        self.logger.debug(" ----------- PEGAR CODIGO")
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

    def burlarcaptcha(self):
        self.logger.debug(" ----------- PEGAR CAPTCHA")
        self.pegarcodigos()
        url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php"
    
        for i in lista_link:
            url = "http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"+i
            formdata = {'aleaNum': '4737', 'aleaValue': 'NDczNw==', 'dtaini': '14/01/2018', 'dtafim':'14/01/2018'}
            os.system('scrapy view '+url+i)
            yield FormRequest.from_response(formdata = formdata,clickdata = {'name': 'commit'},callback = self.after_captcha)

    def after_captcha(self):
        self.logger.debug(" ----------- AFTER CAPTCHA")
        if ("Estação Meteorológica de Observação de Superfície Automática") in response.body:
            self.logger.error("Captcha failed")
            return
    def parse(self, response):
        self.logger.debug(" ----------- PARSE")
        self.burlarcaptcha()
   
