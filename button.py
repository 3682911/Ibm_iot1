import sys
import time
import json
import paho.mqtt.client as mqtt

#MQTT paramenters
host='5t346b.messaging.internetofthings.ibmcloud.com'
clientid='d:5t346b:Buttons:Button'
username='use-token-auth'
password='2KW@f5gNN8&Pw!pLdR'
topic='iot-2/evt/button/fmt/json'

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
b=0

while True:
	try:
		if b<9:
			payload={"b" : "on"}
		else:
			payload={"b" : "off"}
		client.publish(topic, json.dumps(payload))
		print(str(b));
		b=(b+1)%16
		time.sleep(1)
	except IOError:
		print("Error")

client.loop()
client.disconnect()
