#!/usr/bin/env python2.7
import time
import os
import requests
from termcolor import colored



try:

 os.system('figlet [+] Coded BY No_One [+]')

except:
    pass


def scanm():
    start = colored("\n\033[92m[\033[91mscan\033[92m]\033[93m$>")
    ips = raw_input(start+"\n\t\033[92m Enter Your List IPS or List Site\033[91m:")
    ips = open(ips, 'r')
    for i in ips.readlines():
        done = i.rstrip()
        try:
               done = done.rstrip()
               bing = requests.get('http://api.hackertarget.com/reverseiplookup/?q='+done)
               if '.' in bing.content:
                         print("\n\033[1;92m[Site]\033[1;90m====>"+"\033[1;92m"+(bing.content))
                         with open('Sites.txt', 'a') as o:
                            o.writelines(bing.content + '\n')
               else:
                      print ("\n\t\033[1;91mError!")
        except:
               pass





