#!/usr/bin/python
# -*- coding: utf-8 -*-
# Thefacesite
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Thefacesite

import os, sys, time
from time import sleep
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

example = """\x1b[103;90;1m[         Thefacesite, My Github: @stepbystepexe         ]\033[0m"""

logo = """
 \033[0;92m▀▀█▀▀ █  █ █▀▀▀ \033[0;94m█▀▀▀ █▀▀█ █▀▀▀ █▀▀▀ \033[0;37m█▀▀▀ ▀█▀ ▀▀█▀▀ █▀▀▀
 \033[0;92m  █   █▀▀█ █▀▀  \033[0;94m█▀▀▀ █▀▀█ █    █▀▀  \033[0;37m▀▀▀█  █    █   █▀▀
 \033[0;92m  ▀   ▀  ▀ ▀▀▀▀ \033[0;94m▀    ▀  ▀ ▀▀▀▀ ▀▀▀▀ \033[0;37m▀▀▀▀ ▀▀▀   ▀   ▀▀▀▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def space(o):
        x = 0
        while x <= o:
                print " ",
                x += 1

def getlink():
        os.system('clear')
        os.system('reset')
        sleep(1)
        print
        print(logo)
        print(example)
        print
        write("\033[0m[ \033[32mINFO \033[0m] \033[3mSaya tidak real kalo code program saya ini ditiru")
        write("         Seburuk apaun itu tolong hargai karya milik orang\033[0m\n\n")
        x = open("vuln.txt","r");
        time.sleep(1)
        link = raw_input('\033[0m[\033[41;77;1m Website \033[0m] ')
        print
        write("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek Web Server ...")
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
                        print '\033[0m[\033[94;1m#\033[0m] \033[77;1mMencoba\x1b[0m: ',i

os.system('clear')
os.system('reset')
sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mDeface Website")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 deface'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
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
    sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    sleep(1)
    restart()
