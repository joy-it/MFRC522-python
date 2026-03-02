#!/usr/bin/env python 
# import libraries
import gpiozero
from JoyIT_RC522 import SimpleMFRC522 

# initialize object for rfid module
reader = SimpleMFRC522() 

# get input to write on tag
text = input('Enter a input:') 
print("Hold the tag to the sensor:")

# write input on tag
reader.write(text) 

# print after sucessfully written
print("Successfully written.") 
