#!/usr/bin/env python
# Code verified on Python 3.7.3
# Created by:Jacque Wilson
# Date: 29/08/2022

import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522
import time
import json

#reading

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()