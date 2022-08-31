#!/usr/bin/env python
# Code verified on Python 3.7.3
# Created by:Jacque Wilson
# Date: 29/08/2022

import paho.mqtt.client as mqtt 
import os

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("iot")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic: {} / Message: {}".format(msg.topic,str(msg.payload.decode("UTF-8"))))
    if(msg.payload.decode("UTF-8") == "Reply"):
        client.publish("python", os.environ.get('OS',''))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Use the IP address of your MQTT server here
SERVER_IP_ADDRESS = "192.168.68.2"
client.connect(SERVER_IP_ADDRESS, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
