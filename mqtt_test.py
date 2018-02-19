#!/usr/bin/python
import json
import time
import paho.mqtt.client as mqtt
from dados_estacao import pegarestacoes
from craw import try_captcha


def on_log(client, userdata, level, buf):
    print(buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection", rc)
        client.loop_stop()


def on_disconnect(client, userdata, rc):
    print("client disconnected OK")


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


count = 0
mqtt.Client.connected_flag = False  # criando flag para conexão
mqtt.Client.suppress_pullback_flag = False
client = mqtt.Client("mqtt-ThingsBoard")  # criando instancia do MQTT
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

broker = "127.0.0.1"
port = 1883
topic = "v1/devices/me/telemetry"

# acess token do device no things board
token = "PUxKME7iXgZWNgqX1vqH"

if token != "":
    pass

client.username_pw_set(token)
client.connect(broker, port)  # estabelecendo conexão

while not client.connected_flag:  # loop de espera para conexão
    client.loop()
    time.sleep(1)

time.sleep(3)
data = dict()

# for i in range(24):
#     data["hora"] = "0"
#     data["temp_min"] = "-"
#     data["temp_max"] = "-"
#     data["temp_inst"] = "-"
#     data["pressao"] = "-"
#     data["radiacao"] = "-"
#     data["vento_vel"] = "-"
#     data["vento_rajada"] = "-"
#     data["data"] = "-"
#     data["latitude"] = "-"
#     data_out = json.dumps(data)  # criação do objeto JSON
#     print("publish topic", topic, "data out= ", data_out)
#     ret = client.publish(topic, data_out, 0)  # publicação
#     time.sleep(5)
#     client.loop()

client.disconnect()

dic = pegarestacoes()
print(dic.keys())
first = list(dic.keys())
print()
first = first[0]
print(try_captcha)
