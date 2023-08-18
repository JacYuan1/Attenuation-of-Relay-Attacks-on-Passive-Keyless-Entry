# Libraries
import time
from RFM69 import Radio, FREQ_915MHZ

# Networking info
CAR = 1
NETWORK = 100
KEYFOB = 2

def carListener():
    with Radio(FREQ_915MHZ, CAR, NETWORK, isHighPower=True, verbose=False,
               interruptPin=24, resetPin=25, spiDevice=0, use_board_pin_numbers=False) as radio:
        print ("Car is on...")

        while True:
            packetBegin = time.time()
            # After sending packet to keyfob, wait at most 10 seconds for a response from keyfob
            while time.time() - packetBegin < 10:

                # Calculate time remaining
                timeTillTimeout = max(0, packetBegin + 10 - time.time())

                # Loop will freeze until we receive packet OR if the time limit is exceeded
                packet = radio.get_packet(timeout = timeTillTimeout)

                # If time limit is exceeded, distance bounding is failed and None is returned.
                if packet is not None:
                # Process packet
                    print(packet)
                    print ("Unlock packet received! Unlocking car doors!")
                    return(1)
                else:
                    print("Failed to receive packet in time, car doors will remain locked...")
                    return(0)

                # Send new packet to keyfob and await response
                if radio.send(KEYFOB, "HELLO KEYFOB", attempts=1, waitTime=100):
                    print("Packet sent!")
                else:
                # If keyfob is out of range or asleep due to accelerometer, try again
                    print ("No response from keyfob, trying again...")

if __name__ == "__main__":
    print("Note - gui_car.py is not the main program. Please run car_door_sim.py.")
