# -*- coding: utf-8 -*-

def pegarestacoes():
    estacoes = {}

    lat, lng, altitude = 0, 0, 0
    codigo, estado, cidade, nome_estacao = "", "", "", ""

    arq = open("estacoes_utf-8.txt", "r")

    for linha in arq:
        linha = linha.replace('\n', '')

        if ("//************* ESTACÃO " in linha):
            comeco_estacao = linha.find("O")
            fim_estacao = linha.find(" *")
            nome_estacao = linha[comeco_estacao + 2:fim_estacao]

        if ("var point" in linha):
            lat_lng = linha.strip(",")
            comeco_lat_lng = lat_lng.find("(")
            fim_lat_lng = lat_lng.find(")")
            lat_lng = lat_lng[comeco_lat_lng + 1:fim_lat_lng]
            lat_lng = lat_lng.split(",")
            lat = lat_lng[0]
            lng = lat_lng[1]

        if ("http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?" in linha):
            comeco_codigo = linha.find("http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?")
            fim_codigo = linha.find("==")
            codigo = linha[comeco_codigo + len("http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"):fim_codigo]

        if ("Altitude: " in linha):
            comeco_altitude = linha.find("Altitude: ")
            fim_altitude = linha.find("metros")
            altitude = linha[comeco_altitude + 10:fim_altitude]

        if ("var label = '" in linha):
            comeco_endereco = linha.find("'")
            fim_endereco = linha.find("'; ")
            endereco = linha[comeco_endereco + 1:fim_endereco]
            endereco = endereco.replace(" ", "")
            endereco = endereco.split("-")
            estado = endereco[0]
            cidade = endereco[1]

            estacoes[nome_estacao] = {'codigo': codigo, 'lat': lat, 'lng': lng, 'cidade': cidade, 'estado': estado,
                                      'altitude': altitude}

    arq.close()

    return estacoes
