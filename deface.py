#!/usr/bin/python
# -*- coding: utf-8 -*-
# Deface
# Coded by Senja
# Github: gitbub.com/thedarksec/Deface

import os, sys, time, marshal
from urllib2 import Request, urlopen, URLError, HTTPError

os.system('clear')
os.system('reset')
time.sleep(1)

exec(marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s\n\x00\x00\x00d\x00\x00Z\x00\x00d\x01\x00S(\x02\x00\x00\x00s\x81\x01\x00\x00\n\n    \x1b[0;32m\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80   \x1b[0;35m\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80   \x1b[0;37m\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\n    \x1b[0;32m \xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80   \x1b[0;35m\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88   \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80   \x1b[0;37m\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\n    \x1b[0;32m \xe2\x96\x80  \xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80   \x1b[0;35m\xe2\x96\x80   \xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80   \x1b[0;37m\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80  \xe2\x96\x80  \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\nN(\x01\x00\x00\x00t\x04\x00\x00\x00logo(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00t\x00\x00\x00\x00t\x08\x00\x00\x00<module>\x06\x00\x00\x00R\x01\x00\x00\x00'))
print (logo)

def space(o):
        x = 0
        while x<=o:
                print " ",
                x+=1

def write(f):
    for e in f + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def lines():
        f = open("finder.txt","r");
        print ('\x1b[0m[\x1b[94;1m#\x1b[0m] Deface Website Attacker')
        print ('\x1b[0m[\x1b[93;1m*\x1b[0m] Coded by Senja')
        print ('\x1b[0m[\x1b[96;1m&\x1b[0m] My Github: @thedarksec')
        time.sleep(1)
        print
        link = raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mWeb Targets\x1b[0m: ')
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
