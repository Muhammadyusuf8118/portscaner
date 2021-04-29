#!/usr/bin/python

import socket
from termcolor import colored

internet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(15)

host = input("<<<<<<-[#]->>>>>> IP?:  ")
#port = int(raw_input("<<<<<<-[#]->>>>>> PORT?:  "))

def portscaner(port):
	if internet.connect_ex((host, port)):
		print(colored("%d porti yopiq ekan" % (port), 'red' ))
	else:
		print(colored("%d porti ochiq ekan" % (port), 'green'))



for port in range(20,100):
	portscaner(port)
