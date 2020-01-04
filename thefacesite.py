#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Thefacesite
# Coded by Senja
# Github: https://github.com/stepbystepexe/Thefacesite
from __opt__ import *
import os, sys, time, marshal
from urllib2 import Request, urlopen, URLError, HTTPError
os.system('clear')
os.system('reset')
time.sleep(1)
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
        f = open("vuln.txt","r");
        print
        print (logo)
        print ('\x1b[103;90;1m[        The Face Site v1.0, Coded by @stepbystep        ]\033[0m')
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
