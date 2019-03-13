#!/usr/bin/env python2.7
import os
import sys
import time
import random
from termcolor import colored



def Index():
    ins = colored(""" \033[1;91m
         ...     ...                                       ....                                  
  .=*8888n.."%888:                                 .x~X88888Hx.                              
 X    ?8888f '8888          u.                    H8X 888888888h.      u.    u.              
 88x. '8888X  8888>   ...ue888b                  8888:`*888888888:   x@88k u@88c.      .u    
'8888k 8888X  '"*8h.  888R Y888r                 88888:        `%8  ^"8888""8888"   ud8888.  
 "8888 X888X .xH8     888R I888>               . `88888          ?>   8888  888R  :888'8888. 
   `8" X888!:888X     888R I888>               `. ?888%           X   8888  888R  d888 '88%" 
  =~`  X888 X888X     888R I888>                 ~*??.            >   8888  888R  8888.+"    
   :h. X8*` !888X    u8888cJ888                 .x88888h.        <    8888  888R  8888L      
  X888xX"   '8888..:  "*888*P"                  '  8888888x..  .x    "*88*" 8888" '8888c. .+ 
:~`888f     '*888*"     'Y"                    `    `*888888888"       ""   'Y"    "88888%   
    ""        `"`                                      ""***""                       "YP'    
                                                                                             
                                 8888888888888 """,)
    ins2 = colored('''                                                                                                                            
NNNNNNNN        NNNNNNNN                                              OOOOOOOOO                                           
N:::::::N       N::::::N                                            OO:::::::::OO                                         
N::::::::N      N::::::N                                          OO:::::::::::::OO                                       
N:::::::::N     N::::::N                                         O:::::::OOO:::::::O                                      
N::::::::::N    N::::::N   ooooooooooo                           O::::::O   O::::::Onnnn  nnnnnnnn        eeeeeeeeeeee    
N:::::::::::N   N::::::N oo:::::::::::oo                         O:::::O     O:::::On:::nn::::::::nn    ee::::::::::::ee  
N:::::::N::::N  N::::::No:::::::::::::::o                        O:::::O     O:::::On::::::::::::::nn  e::::::eeeee:::::ee
N::::::N N::::N N::::::No:::::ooooo:::::o                        O:::::O     O:::::Onn:::::::::::::::ne::::::e     e:::::e
N::::::N  N::::N:::::::No::::o     o::::o                        O:::::O     O:::::O  n:::::nnnn:::::ne:::::::eeeee::::::e
N::::::N   N:::::::::::No::::o     o::::o                        O:::::O     O:::::O  n::::n    n::::ne:::::::::::::::::e 
N::::::N    N::::::::::No::::o     o::::o                        O:::::O     O:::::O  n::::n    n::::ne::::::eeeeeeeeeee  
N::::::N     N:::::::::No::::o     o::::o                        O::::::O   O::::::O  n::::n    n::::ne:::::::e           
N::::::N      N::::::::No:::::ooooo:::::o                        O:::::::OOO:::::::O  n::::n    n::::ne::::::::e          
N::::::N       N:::::::No:::::::::::::::o                         OO:::::::::::::OO   n::::n    n::::n e::::::::eeeeeeee  
N::::::N        N::::::N oo:::::::::::oo                            OO:::::::::OO     n::::n    n::::n  ee:::::::::::::e  
NNNNNNNN         NNNNNNN   ooooooooooo                                OOOOOOOOO       nnnnnn    nnnnnn    eeeeeeeeeeeeee  
                                         ________________________                                                         
                                         _::::::::::::::::::::::_                                                         
                                         ________________________                                                         
                                                                                                                          
                                                                                                                          
                                                                            ''', 'green')

    ins3 = colored(''' \033[1;90m
    M"""""""`YM                       MMP"""""YMM                   
    M  mmmm.  M                       M' .mmm. `M                   
    M  MMMMM  M .d8888b.              M  MMMMM  M 88d888b. .d8888b. 
    M  MMMMM  M 88'  `88              M  MMMMM  M 88'  `88 88ooood8 
    M  MMMMM  M 88.  .88              M. `MMM' .M 88    88 88.  ... 
    M  MMMMM  M `88888P'              MMb     dMM dP    dP `88888P' 
    MMMMMMMMMMM         NO_One Script MMMMMMMMMMM  
        ''')

    insm = [ins, ins2, ins3]
    const = insm[random.randint(0, 2)]
    print(const)


