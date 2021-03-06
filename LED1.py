import sys
import time
import json
import paho.mqtt.client as mqtt

#MQTT paramenters
host='5t346b.messaging.internetofthings.ibmcloud.com'
clientid='d:5t346b:Bulbs:LED1'
username='use-token-auth'
password='*NNopP_lsOCCzTw4hm'
topic='iot-2/cmd/+/fmt/json'

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
	button=json.loads(msg.payload)["buttonState"]
	temperature=json.loads(msg.payload)["temperatureState"]
	if button == "on":
		print("LED_ON");
	else:
		print("LED_OFF");
	if temperature<11:
		print("fa freddo");
	else:
		print("fa caldo");

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
client.subscribe(topic)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
