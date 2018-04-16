import sys
import time
import json
import ibmiotf.application
#import paho.mqtt.client as mqtt

options = {
"org": "5t346b",
"id": "App1",
"auth-method": "apikey",
"auth-key": "a-5t346b-ywsegl3jwk",
"auth-token": "!&&w?RQ@Bq4hH@KWi4",
"clean-session": True
}

sourceDeviceTypeTemp="Sensors"
sourceDeviceIdTemp="TemperatureSensor"
sourceEventTemp="temperature"

sourceDeviceTypeUmid="Sensors"
sourceDeviceIdUmid="UmiditySensor"
sourceEventUmid="umidity"

targetDeviceType="Bulbs"
targetDeviceId="LED1"

def Callback(event):
	print "Got event " + json.dumps(event.data)
	if event.deviceId == 'UmiditySensor':
		print "value" + json.dumps(event.data['u'])
		umidity= event.data['u']
		commandDataUmid={'umidityState' : umidity}
		client.publishCommand(targetDeviceType, targetDeviceId, "umidityState", "json", commandDataUmid)
	else:
		print "value" + json.dumps(event.data['t'])	
		temperature= event.data['t']
		commandDataTemp={'temperatureState' : temperature}
		client.publishCommand(targetDeviceType, targetDeviceId, "temperatureState", "json", commandDataTemp)

client = ibmiotf.application.Client(options)
client.connect()
client.deviceEventCallback = Callback

client.subscribeToDeviceEvents(sourceDeviceTypeTemp, sourceDeviceIdTemp, sourceEventTemp)

client.subscribeToDeviceEvents(sourceDeviceTypeUmid, sourceDeviceIdUmid, sourceEventUmid)

while True:
	time.sleep(1)
