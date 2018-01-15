import urllib
url = "http://www.inmet.gov.br/sonabra/maps/pg_mapa.php"
f = urllib.urlopen(url)
#source_code = f.read()
n = 0
z = 0
while True:
    z +=1
    source_code = f.readline()
    n = source_code.find("//*************")
    if n != -1:
        break        
    
lista = []
while True:
    source_code = f.readline()
    t = source_code.find("(")
    lista.append(source_code[t:-2:])
    t = source_code.find("Estação")
    auxiliar = source_code[t:-1:]
    t = auxiliar.find("<br>")
    y = auxiliar.find("</b")
    lista.append(auxiliar[y+4:t:])
    

    n = source_code.find("//*************")
    if n != -1:
        break
    

print (z)
print (lista)

#source_code = source_code.split("\n")  
#print source_code[63]
#pos = 63
#for i range 8:
    
#    source_code[pos]


## começo de estação: //************* contar oito linhas
## dar \n
## parâmetros para o postman(no body):
## aleaValue: endereço da imagem
## aelaNum: valor numérico da imagem
## dtaini: data da requisição
## dtafim: data final da requisição
## endereço do link: http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php
## obs: dtaini e dtafim podem não ser necessários  
