#!/usr/bin/env python 
# import libraries
import gpiozero 
from JoyIT_RC522 import SimpleMFRC522 

# initialize object for rfid module
reader = SimpleMFRC522() 

# get id and text from tag
id, text = reader.read()

# print tag id and text
print(id) 
print(text) 
