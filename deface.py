#!/usr/bin/python
# Defaceweb
# Coded by Senja
# Github: gitbub.com/thesixtynine/Defaceweb

import os, sys, time
from urllib2 import Request, urlopen, URLError, HTTPError

os.system('clear')
os.system('reset')
time.sleep(1)

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1

def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

logo = '''\x1b[77;1m

:::::::-.  .,:::::: .-:::::` :::.       .,-::::: .,::::::
 ;;,   `';,;;;;```` ;;;````  ;;`;;    ,;;;'````' ;;;;````
 `[[     [[ [[cccc  [[[,,== ,[[ '[[,  [[[         [[cccc
  $$,    $$ $$""""  `$$$"``c$$$cc$$$c $$$         $$""""
  888_,o8P` 888oo,__ 888    888   888,`88bo,__,o, 888oo,__
  MMMMP"`   """"YUMMM"MM,   YMM   ""`   "YUMMMMMP"""""YUMM

'''

print (logo)

def lines():
        f = open("datapages.txt","r");
        print ('\x1b[0m[\x1b[94;1m#\x1b[0m] Deface Website Attacker')
        print ('\x1b[0m[\x1b[93;1m*\x1b[0m] Coded by Senja')
        print ('\x1b[0m[\x1b[96;1m&\x1b[0m] My Github: @thesixtynine')
        time.sleep(1)
        print
        link = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mWeb Targets\x1b[0m: ')
        print
        write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mChecking Link ...')
        print
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = 'http://'+link+'/'+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print '\x1b[0m[=\x1b[42;90;1m INT \x1b[0m=] \x1b[77;1;3mCheck\x1b[0m: ',req_link
lines()
sys.exit(1)
