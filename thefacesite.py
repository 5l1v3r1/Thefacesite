#!/usr/bin/python
# -*- coding: utf-8 -*-
# Thefacesite
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Thefacesite

from __opt__ import *
import os, sys, time, marshal
from urllib2 import Request, urlopen, URLError, HTTPError

info = """
Nama        : Thefacesite
Versi       : 2.6 (Update: 23 Januari 2020, 8:30 PM)
Tanggal     : 12 Juli 2019
Author      : Nedi Senja
Tujuan      : Mendeface Website dengan
              menacri admin login
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\x1b[103;90;1m[       The Face Site, My Github: @stepbystepexe         ]\033[0m"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def space(o):
        x = 0
        while x <= o:
                print " ",
                x += 1

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def getlink():
        x = open("vuln.txt","r");
        print
        time.sleep(1)
        print
        link = raw_input('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mMasukan Web Target\x1b[0m: ')
        print
        write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMengecek Link ...')
        print
        while True:
                o = x.readline()
                if not o:
                        break
                i = 'http://'+link+'/'+o
                r = Request(i)
                try:
                        response = urlopen(r)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print '\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1;3mMencobak\x1b[0m: ',i

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[1;96mあ\033[0m] \033[1;77mMulai Menggunakan Thefacesite")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option.strip() in 'あ 1 gunakan'.split():
    getlink()
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Deface')
    print(info)
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()
