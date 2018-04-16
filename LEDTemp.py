import sys
import time
import json
import paho.mqtt.client as mqtt

#MQTT paramenters
host='5t346b.messaging.internetofthings.ibmcloud.com'
clientid='d:5t346b:Bulbs:LED1'
username='use-token-auth'
password='*NNopP_lsOCCzTw4hm'
topic='iot-2/cmd/temperatureState/fmt/json'

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
	temperature=json.loads(msg.payload)["temperatureState"]
	print(temperature);
	if temperature<11:
		print("temperatura BASSA");
	else:
		print("temperatura ALTA");

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
client.subscribe(topic)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
