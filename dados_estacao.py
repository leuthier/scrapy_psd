# -*- coding: utf-8 -*-

import json

def pegarestacoes():
    estacoes = {}
    aux = {}
    qtdade = 0
    
    lat, lng, altitude = 0, 0, 0
    codigo, estado, cidade, nome_estacao = "","","",""

    arq = open("estacoes.txt","r")

    for linha in arq:
        linha = linha.replace('\n','')
##    print("linha",linha)
        
##pegar nome da estacao
        if ("//************* ESTACÃO " in linha):
            comeco_estacao = linha.find("O")
            fim_estacao = linha.find(" *")        
            nome_estacao = linha[comeco_estacao+2:fim_estacao]
##            estacoes['nome'] = nome_estacao
##            print("nome estacao",nome_estacao)


        ##    pegar latitude e longitude da estacao
        if ("var point" in linha):
            lat_lng = linha.strip(",")
            comeco_lat_lng = lat_lng.find("(")
            fim_lat_lng = lat_lng.find(")")
            lat_lng = lat_lng[comeco_lat_lng+1:fim_lat_lng]
            lat_lng = lat_lng.split(",")
            lat = lat_lng[0]
            lng = lat_lng[1]
##            aux['lat'] = lat
##            aux['lng'] = lng
##            print("latlng",lat_lng)


        ##  pegar codigo das estacoes
        if ("http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?" in linha):
            comeco_codigo = linha.find("http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?")
            fim_codigo = linha.find("==")
            codigo = linha[comeco_codigo+len("http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?"):fim_codigo]
##            aux['codigo'] = codigo
##            print ("codigo",codigo)


        ##    pegar estado/cidade da estacao
        if ("var label = '" in linha):
            comeco_endereco = linha.find("'")
            fim_endereco = linha.find("'; ")
            endereco = linha[comeco_endereco+1:fim_endereco]
            endereco = endereco.replace(" ","")
            endereco = endereco.split("-")
##            print("endereco:",endereco)
            estado = endereco[0]
            cidade = endereco[1]
##            aux['estado'] = estado
##            aux['cidade'] = cidade
            print("estado-cidade:",estado+"-"+cidade)
            qtdade += 1
            print("enderecos",qtdade)

            
        ##  pegar altitude
        if ("Altitude: " in linha):
            comeco_altitude = linha.find("Altitude: ")
            fim_altitude = linha.find("metros")
            altitude = linha[comeco_altitude+10:fim_altitude]
##            aux['altitude'] = altitude
##            print("altitude",altitude)


##        print("nome_estacao",nome_estacao)
##        print("estacoes[nome_estacao]",estacoes[nome_estacao])
            estacoes[nome_estacao] = {'codigo':codigo,'lat':lat,'lng':lng,'cidade':cidade,'estado':estado,'altitude':altitude,}
        
    print("estacoes['C891']",estacoes['C891'])
##        print ("est [nome]",estacoes[estacao_nome])
       


##        saida_json = json.dumps(estacoes[nome_estacao])
##    for a in estacoes:
##        arq_saida = open("estacoes.json","w")
##        arq_saida.write(a)
##        arq_saida.close()
        
    arq.close()
    
    
    return None


pegarestacoes()
