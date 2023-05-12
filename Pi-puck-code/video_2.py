#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from smbus2 import SMBus, i2c_msg
import sys
import time

I2C_CHANNEL = 12
LEGACY_I2C_CHANNEL = 4
ROB_ADDR = 0x1F
ACTUATORS_SIZE = (19+1) # Data + checksum.
SENSORS_SIZE = (46+1) # Data + checksum.

actuators_data = bytearray([0] * ACTUATORS_SIZE)
sensors_data = bytearray([0] * SENSORS_SIZE)
prox = [0 for x in range(8)]
prox_amb = [0 for x in range(8)]
mic = [0 for x in range(4)]
mot_steps = [0 for x in range(2)]

def update_robot_sensors_and_actuators():
	global sensors_data
	global actuators_data
	try:
		write = i2c_msg.write(ROB_ADDR, actuators_data)
		read = i2c_msg.read(ROB_ADDR, SENSORS_SIZE)
		bus.i2c_rdwr(write, read)
		sensors_data = list(read)
	except:
         print(":(")
		#sys.exit(1)

try:
	bus = SMBus(I2C_CHANNEL)
except:
	try:
		bus = SMBus(LEGACY_I2C_CHANNEL)
	except:
		print("Cannot open I2C device")
		#sys.exit(1)
        
        
def forward():
    actuators_data[0] = 0		# Left speed: 512
    actuators_data[1] = 2
    actuators_data[2] = 0		# Right speed: 512
    actuators_data[3] = 2
    
def forwardf():
    actuators_data[0] = 0		# Left speed: 1024
    actuators_data[1] = 4
    actuators_data[2] = 0		# Right speed: 1024
    actuators_data[3] = 4

def back():
    actuators_data[0] = 0		# Left speed: -512
    actuators_data[1] = 0xFE
    actuators_data[2] = 0		# Right speed: -512
    actuators_data[3] = 0xFE
        
def left():
    actuators_data[0] = 0		# Left speed: 0
    actuators_data[1] = 0
    actuators_data[2] = 0		# Right speed: 512
    actuators_data[3] = 2
    
def right():
    actuators_data[0] = 0		# Left speed: 512
    actuators_data[1] = 2
    actuators_data[2] = 0		# Right speed: 0
    actuators_data[3] = 0
    
def stop():
    actuators_data[0] = 0		# Left speed: 0
    actuators_data[1] = 0
    actuators_data[2] = 0		# Right speed: 0
    actuators_data[3] = 0
    actuators_data[4] = 0 		# Speaker sound
    actuators_data[5] = 0	    # LED1, LED3, LED5, LED7 on/off flag
    actuators_data[6] = 0		# LED2 red
    actuators_data[7] = 0		# LED2 green
    actuators_data[9] = 0		# LED4 red
    actuators_data[8] = 0		# LED2 blue
    actuators_data[10] = 0	    # LED4 green
    actuators_data[11] = 0		# LED4 blue
    actuators_data[12] = 0	    # LED6 red
    actuators_data[13] = 0	    # LED6 green
    actuators_data[14] = 0		# LED6 blue
    actuators_data[15] = 0	    # LED8 red
    actuators_data[16] = 0	    # LED8 green
    actuators_data[17] = 0		# LED8 blue
    actuators_data[18] = 0 		# Settings.

actuators_data[0] = 0		# Left speed: 0
actuators_data[1] = 0
actuators_data[2] = 0		# Right speed: 0
actuators_data[3] = 0
actuators_data[4] = 0 		# Speaker sound
actuators_data[5] = 0x0		# LED1, LED3, LED5, LED7 on/off flag
actuators_data[6] = 100		# LED2 red
actuators_data[7] = 100		# LED2 green
actuators_data[9] = 100		# LED4 red
actuators_data[8] = 0		# LED2 blue
actuators_data[10] = 100	# LED4 green
actuators_data[11] = 0		# LED4 blue
actuators_data[12] = 100	# LED6 red
actuators_data[13] = 100	# LED6 green
actuators_data[14] = 0		# LED6 blue
actuators_data[15] = 100	# LED8 red
actuators_data[16] = 100	# LED8 green
actuators_data[17] = 0		# LED8 blue
actuators_data[18] = 0 		# Settings.

time.sleep(7)

counter = 0
start = time.time()
timer = start + 4
print(counter)

while 1:
    if (counter == 0):
        forward()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 5
    elif (counter == 1):
        left()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 11
    elif (counter == 2):
        forward()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 1
    elif (counter == 3):
        right()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 7.5
    elif (counter == 4):
        forward()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 2.35
    elif (counter == 5):
        left()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 7.5
    elif (counter == 6):
        back()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 5.875
    elif (counter == 7):
        right()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 10
    elif (counter == 8):
        back()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 2.35
    elif (counter == 9):
        left()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 5
    elif (counter == 10):
        forwardf()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 1.175
    elif (counter == 11):
        right()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 5
    elif (counter == 12):
        forward()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 4.7
    elif (counter == 13):
        right()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 10      
    elif (counter == 14):
        forward()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 1.175
    elif (counter == 15):
        right()
        if (time.time() > timer):
            counter += 1
            print(counter)
            start = time.time()
            timer = start + 6
    elif (counter == 16):
        forwardf()
        if (time.time() > timer):
            stop()
            counter += 1
            print(counter)
   
    checksum = 0
    for i in range(ACTUATORS_SIZE-1):
   	  checksum ^= actuators_data[i]		
   	  actuators_data[ACTUATORS_SIZE-1] = checksum

   	  update_robot_sensors_and_actuators()
    
    if (counter == 17):
        time.sleep(1)
        print("End")
        break
    
    
    