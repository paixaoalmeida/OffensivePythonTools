import socket      #PortScan que scaneia as portas de acordo com uma lista usando um For loop, retorna se a porta está aberta e se tiver, o banner
import sys         #serviço


portas_lis = [20, 21, 22, 23, 25, 80, 443, 110, 3389]  #Lista para as portas

for portas in portas_lis: #For loop para ler a lista e fazer as conexões
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #biblioteca socket
    res = meusocket.connect_ex((sys.argv[1],portas))
    
    if (res == 0):  #Se for 0 então a porta está ativa
        print("Porta" ,portas, "Aberta \n")
        servico = meusocket.recv(1024) #Receber a resposta (no caso o banner da porta)
        print(f"Serviço rodando na porta -----> {portas} ------> {servico} \n")
        meusocket.close() #Fechar a conexão



