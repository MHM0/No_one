#!/usr/bin/python2.7

import os
import sys
import time
import datetime
sys.path.append('moudules/')
from index import *
from admin import *
from ddos import *
from scan import *
from gost import *
from command import *
from page import *





try:
    from termcolor import colored, cprint
    os.system('c')
    #os.system('clear')


except ImportError as ie:
    print (str(ie))




class mhmMain(object):

    def root(selfs):
        __version__ = '1.0.0'
        __Facebook__ = "https://facebook.com/mhm.hack"
        __date__ = datetime.datetime.now()
        __tools__ = "3"

        try:
            gonow = raw_input("\n\033[92m[\033[91mmhm\033[92m]\033[93m$>")

            if gonow == 'exit':
                print('\033[91mThanks for Usage \033[96mmhmv1!')
                sys.exit(0)

            if gonow == 'clear':
               Index()
               GostIndex()
               return mhm.root()

            if gonow == 'panel':
                adminm()
                return mhm.root()

            if gonow == 'scan':
                scanm()
                return mhm.root()

            if gonow == 'ddos':
               ddosm()
               return mhm.root()

            if gonow == 'help':
                cmd()
                return mhm.root()

            if gonow == 'show modules':
                modules()
                return mhm.root()
            if gonow == 'page':
                page()
                return mhm.root()


        except KeyboardInterrupt:
            cprint("\n [!] You Press Ctrl + C! To Quit.", 'red')
            sys.exit(1)
        except:
             pass


def index():
    Index()
    GostIndex()

if __name__ == "__main__":
    Index()
    GostIndex()
    mhm = mhmMain()
    mhm.root()





