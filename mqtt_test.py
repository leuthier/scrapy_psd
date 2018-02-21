#!/usr/bin/python
import json
import time
import paho.mqtt.client as mqtt
from dados_estacao import pegarestacoes
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
    id = 0
    for _ in credentials:
        client.username_pw_set(credentials[id])
        client.connect(broker, port)  # estabelecendo conexão
        id += 1

        while not client.connected_flag:  # loop de espera para conexão
            client.loop()
            time.sleep(1)

        time.sleep(2)
        data = dict()
        day_list = try_captcha()

        hour = 0
        for i in range(24):
            data["hora"] = day_list[int(hour)]['hora']
            data["temp_min"] = day_list[int(hour)]['temp_min']
            data["temp_max"] = day_list[int(hour)]['temp_max']
            data["temp_inst"] = day_list[int(hour)]['temp_inst']
            data["pressao"] = day_list[int(hour)]['pressao']
            data["radiacao"] = day_list[int(hour)]['radiacao']
            data["vento_vel"] = day_list[int(hour)]['vento_vel']
            data["vento_rajada"] = day_list[int(hour)]['vento_rajada']
            data["data"] = day_list[int(hour)]['data']
            data_out = json.dumps(data)  # criação do objeto JSON
            print("publish topic", topic, "data out= ", data_out)
            ret = client.publish(topic, data_out, 0)  # publicação
            time.sleep(4)
            hour += 1
            client.loop()

    client.disconnect()


# publish_mqtt()
day_list = try_captcha()
print(day_list)
# hour = 0
# for i in range(24):
#     print(day_list[int(hour)]['hora'])
#     hour += 1
