#!/usr/bin/env python
# Code verified on Python 3.7.3
# Created by:Jacque Wilson
# Date: 29/08/2022

import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('New data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")
finally:
    GPIO.cleanup()