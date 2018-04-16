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

sourceDeviceType="Buttons"
sourceDeviceId="Button"
sourceEvent="button"

targetDeviceType="Bulbs"
targetDeviceId="LED1"

def ButtonCallback(event):
	print "Got event " + json.dumps(event.data)
	button= event.data['b']
	commandData={'buttonState' : button}	
	client.publishCommand(targetDeviceType, targetDeviceId, "buttonState", "json", commandData)

client = ibmiotf.application.Client(options)
client.connect()
client.deviceEventCallback = ButtonCallback

client.subscribeToDeviceEvents(deviceType=sourceDeviceType, deviceId=sourceDeviceId, event=sourceEvent)

while True:
	time.sleep(1)
