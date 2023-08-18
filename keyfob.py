# This code is the main keyfob code.
# The purpose of this program is to send out packets while the device is in motion to simulate
# a keyfob with motion detection.

# Libraries
import time
from board import SCL, SDA
from busio import I2C
from RFM69 import Radio, FREQ_915MHZ
from adafruit_adxl34x import ADXL345
import threading


# Networking info
KEYFOB = 2
NETWORK = 100
CAR = 1

i2c = I2C(SCL, SDA) #i2c bus
accelerometer = ADXL345(i2c) #Accelerometer model
accelerometer.enable_motion_detection(threshold=20) #Motion threshold

def receivePacket(radio):
    while True:
        # Loop will freeze until a packet is received
        packet = radio.get_packet()
        print("Got a packet: ", end="")
        # Print packet, packet contains various information that can enable further security enhancements
        print(packet)
        


# Motion detection loop, 0 = no signal, 1 - signal
with Radio(FREQ_915MHZ, KEYFOB, NETWORK, isHighPower=True, verbose=False,
           interruptPin=24, resetPin=25, spiDevice=0, use_board_pin_numbers=False) as radio:
    
    # Loop to receive packets      
    receiveThread = threading.Thread(target = receivePacket, args=(radio,))
    receiveThread.start()        
   
   # Detects if keyfob is in motion. If in motion, send the signal. Otherwise, do not send.
    while True:
        if accelerometer.events['motion'] == True:
            print("Motion detected! Sending signal!")
            radio.send(CAR, "UNLOCK", attempts=1, waitTime=100)
            print("Packet sent!")
        else:
            print("No motion detected, not sending signal")
        time.sleep(1)
