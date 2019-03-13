from  urllib2 import urlopen
import os
import sys
from termcolor import colored


def page():
    try:
       send = colored("\n\033[92m[\033[91mpage content\033[92m]\033[93m$> ")
       url = raw_input(send+"\n\t\033[92m Enter The URL \033[91m:")
       if (not url.startswith("http://")) and (not url.startswith("https://")):
           url = "http://" + url
       content = "############# NO ONE #############"+"\n\n" + urlopen(url).read()
       yesorno = raw_input("\n\t\033[92m Are you whoint save page to File (Y/N) \033[91m:")
       if yesorno == 'Y':
           save = raw_input("\n\t\033[92m Save to File \033[91m:")
           print("\n\033[1;92m Save to " + "\033[1;90m"+save)
           save_file = open(save, 'w')
           save_file.write(content)
       elif yesorno == 'N':
          print("\n\033[1;96m" + content)
       else:
           print("\033[1;91mError!")
    except ValueError as er:
        print("\033[1;91mNot a valid URL"+str(er))







