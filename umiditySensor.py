import sys
import time
import json
import paho.mqtt.client as mqtt

#MQTT paramenters
host='5t346b.messaging.internetofthings.ibmcloud.com'
clientid='d:5t346b:Sensors:UmiditySensor'
username='use-token-auth'
password='uwtuShhQdDN)d&Ng3S'
topic='iot-2/evt/umidity/fmt/json'

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
u=0

while True:
	try:
		client.publish(topic, json.dumps({'u':u}))
		print(str(u));
		u=(u+8)%90
		time.sleep(1)
	except IOError:
		print("Error")

client.loop()
client.disconnect()
