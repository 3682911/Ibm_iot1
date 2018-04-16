import sys
import time
import json
import paho.mqtt.client as mqtt

#MQTT paramenters
host='5t346b.messaging.internetofthings.ibmcloud.com'
clientid='d:5t346b:Sensors:TemperatureSensor'
username='use-token-auth'
password=')I*45V-?@Pv)_Moo?N'
topic='iot-2/evt/temperature/fmt/json'

client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
t=0

while True:
	try:
		client.publish(topic, json.dumps({'t':t}))
		print(str(t));
		t=(t+1)%20
		time.sleep(2)
	except IOError:
		print("Error")

client.loop()
client.disconnect()
