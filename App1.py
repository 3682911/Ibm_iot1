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

sourceDeviceType1="Buttons"
sourceDeviceId1="Button"
sourceEvent1="button"

sourceDeviceType2="Sensors"
sourceDeviceId2="TemperatureSensor"
sourceEvent2="temperature"

targetDeviceType="Bulbs"
targetDeviceId="LED1"

def ButtonCallback(event1):
	print "Got event " + json.dumps(event1.data)
	button= event1.data['b']
	commandData={'buttonState' : button}	
	client.publishCommand(targetDeviceType1, targetDeviceId1, "buttonState", "json", commandData)

def ButtonCallback(event2):
	print "Got event " + json.dumps(event2.data)
	temperature= event2.data['t']
	commandData={'temperatureState' : temperature}
	client.publishCommand(targetDeviceType2, targetDeviceId2, "temperatureState", "json", commandData)

client = ibmiotf.application.Client(options)

client.connect()
client.deviceEventCallback = ButtonCallback

client.subscribeToDeviceEvents(deviceType=sourceDeviceType1, deviceId=sourceDeviceId1, event=sourceEvent1)

client.subscribeToDeviceEvents(deviceType=sourceDeviceType2, deviceId=sourceDeviceId2, event=sourceEvent2)

while True:
	time.sleep(1)
