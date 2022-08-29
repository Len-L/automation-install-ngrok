
import os
import time as t
import wget as d

t.sleep(1)
print("1. Install Ngrok 'Debian' ")
print("2. Version")
print("99. keluar or exit")
print(" ")
a = str(input("-> "))

if a=="1":
    url = 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz'
    save = d.download(url)
    print(" ")
    print("Nama File ", save)
    t.sleep(1)
    print(" ")
    print("decompres")
    os.system("tar xvzf ngrok-v3-stable-linux-amd64.tgz")
    print(" ")
    t.sleep(1)
    print("OK")
    print(" ")
if a=="2":
    print(" ")
    print("Version 1.0")
    print(" ")
if a=="99":
    print("bye :) ")



