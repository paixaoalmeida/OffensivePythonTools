import socket
import sys

ip = "192.168.15.1"

porta = 22


meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #biblioteca socket
res = meusocket.connect_ex((ip,porta))
banner = meusocket.recv(1024)

if (res == 0):
    print ("Porta aberta",porta)
else:
    print ("Porta fechada",porta)
print(banner)

    #socket para se conectar a uma porta e ver se ela está fechada ou aberta!
