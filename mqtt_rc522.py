# Purpose Read RFID tags and publish to MQTT
# Created by:Jacque Wilson
# Date: 29/08/2022

import paho.mqtt.client as mqtt #impor for Python MQTT
from mfrc522 import SimpleMFRC522 #import for RFID reader
import RPi.GPIO as GPIO #import for GPIO
import time #import for time

status_topic = "RPi4/7C50/rfid" #MQTT topic for publishing RFID data
event_topic = "RPi4/7C50/rfid" #MQTT topic for subscribing to RFID data
host = "192.168.68.2"   #MQTT server IP address
port = 1883 #MQTT server port
led_red = 20 #GPIO pin for red LED
led_green = 21 #GPIO pin for green LED

def GPIO_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_red, GPIO.OUT)
    GPIO.setup(led_green, GPIO.OUT)
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(led_green, GPIO.LOW)

def LOG(msg):
    print(msg)
    
def mqtt_on_message(client, userdata, message):
    LOG("message received " ,str(message.payload.decode("utf-8")))
    LOG("message topic=",message.topic)
    LOG("message qos=",message.qos)
    LOG("message retain flag=",message.retain)
    if message.payload.decode("utf-8") == "OFF":
        GPIO.output(led_red, GPIO.LOW)
    if message.payload.decode("utf-8") == "ON":
        GPIO.output(led_red, GPIO.HIGH) 

def mqtt_on_connect(client, userdata, flags, rc):
    if rc == 0:
        LOG("Connected to MQTT broker")
        client.publish(status_topic, "Hello from Python!")
    else:
        LOG("Failed to connect, return code %d\n", rc)
        
def mqtt_int():
    protcol = mqtt.MQTTv311
    client_id = "RPi4/7C50/rfid"
    client = mqtt.Client(client_id, clean_session=False, protocol=protcol)
    client.on_connect = mqtt_on_connect
    client.on_message = mqtt_on_message
    #client.connect(host, port)
    #client.loop_start()
    return client

def rfid_read(reader):
    id, text = reader.read()
    return id, text

def main():
    GPIO_init()
    reader = SimpleMFRC522()
    client = mqtt_int()
    client.connect(host, port)
    client.loop_start()
    while True:
        id, text = rfid_read(reader)
        print(id)
        print(text)
        print("#5 is alive")
        GPIO.output(led_green, GPIO.HIGH)
        client.publish(status_topic, text)
        time.sleep(1)
        GPIO.output(led_green, GPIO.LOW)

if __name__=="__main__":
    main() 