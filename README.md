# inmet_psd
Coletor de dados INMET
www.inmet.gov.br/sonabra/maps/pg_mapa.php

navegue até o diretório do projeto:

    
    pip install -r requirements

pagar coletar os dados das estações:
 
    
    python dados_estacao.py
    python craw.py
            
configurar os devices no thingsboard:
    get_token_sys() retorna o token do ThingsBoard;
    create_device() retorna o Id do device criado;
    get_credencial() retorna a Token do device pesquisado;
    publish() publica os dados necessarios para o calculo de evapotranspiração;
    get_telemetry() retorna os dados do device pesquisado, a partir do timeStamp.
    
    
