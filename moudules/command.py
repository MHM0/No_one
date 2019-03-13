#! /usr/bin/env python2.7
import os
from termcolor import colored


def modules():
	print "\n"
	print "\t\033[93m[+] \033[92m All tools\033[33m$\033[91m>"
	print "\n"
	print "\033[93mTools: " + colored("     \t\033[96mDescription")
	print "\033[92mpanel\t" + colored("     \t\033[91mFind the admin control panel")
	print "\033[92mscan\t" + colored("     \t\033[91mExtracts sites that are in the server using the address or site name")
	print "\033[92mddos\t" + colored("     \t\033[91mAn aggressive attack on applications, using port 25")
	print "\033[92mpage\t" + colored("     \t\033[91mGet the raw HTML of a given web page.")

	print "\n"

def cmd():
	print "\n"
	print "\033[92mCommand: " + colored("     \t\033[96mDescription")
	print "\033[92mhelp " + colored("      \t\033[91mShow This Message")
	print "\033[92mexit " + colored("      \t\033[91mExit The script")
	print "\033[92mclear " + colored("    \t\033[91mRestart No_One")
	print "\033[92mshow modules " + colored("\t\033[91mList All Modules")

  
