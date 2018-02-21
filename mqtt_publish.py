#!/usr/bin/python
import json
import time
import paho.mqtt.client as mqtt
from craw import try_captcha
from device_config import create_base_devices



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


mqtt.Client.connected_flag = False  # criando flag para conexão
mqtt.Client.suppress_pullback_flag = False
client = mqtt.Client("mqtt-ThingsBoard")  # criando instancia do MQTT
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

broker = "127.0.0.1"
port = 1883
topic = "v1/devices/me/telemetry"


def publish_mqtt():
    credentials = create_base_devices()
    inc = 0
    dic_master = try_captcha()
    aux = list(dic_master.keys())
    data = dict()
    for k in aux:
        lista = dic_master[aux[inc]]
        client.username_pw_set(credentials[inc])
        client.connect(broker, port)  # estabelecendo conexão

        inc += 1
        hour = 0
        time.sleep(2)
        for i in range(len(lista)):
            data["hora"] = lista[hour]['hora']
            data["temp_min"] = lista[hour]['temp_min']
            data["temp_max"] = lista[hour]['temp_max']
            data["temp_inst"] = lista[hour]['temp_inst']
            data["pressao"] = lista[hour]['pressao']
            data["radiacao"] = lista[hour]['radiacao']
            data["vento_vel"] = lista[hour]['vento_vel']
            data["vento_rajada"] = lista[hour]['vento_rajada']
            data["data"] = lista[hour]['data']
            data_out = json.dumps(data)  # criação do objeto JSON
            print("publish topic", topic, "data out= ", data_out)
            ret = client.publish(topic, data_out, 0)  # publicação
            time.sleep(4)
            hour += 1
    client.disconnect()

publish_mqtt()
