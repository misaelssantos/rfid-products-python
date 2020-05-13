# Cliente MQTT
import os
import sys
import paho.mqtt.client as mqtt
from logger import Logger
from pprint import pprint
from products import ProductList

log = Logger('MQTT')
prods = ProductList()

mqtt_broker = os.getenv('MQTT_BROKER', "industrial.api.ubidots.com")
mqtt_token =  os.getenv('MQTT_TOKEN')
mqtt_port = int(os.getenv('MQTT_PORT', 1883))

if mqtt_token is None:
    log.error("Variavel MQTT_TOKEN tem que ser configurada")
    sys.exit(1)

topic_subscribe = "/v1.6/devices/esp32/+/lv"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    log.info("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic_subscribe)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    log.info(f'Msg Recebida: {msg.topic} {str(msg.payload)}')
    tag = extract_tag(msg.topic)
    # parsing the value
    strvalue = msg.payload.decode('utf-8')
    value = int(strvalue) if strvalue.isdigit() else None 
    # updating database...
    prods.update(tag, value)

def extract_tag(topic):
    parts = topic.split("/")
    tag = parts[len(parts)-2]
    return tag

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(mqtt_token, password=None)
client.connect(mqtt_broker, mqtt_port, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()