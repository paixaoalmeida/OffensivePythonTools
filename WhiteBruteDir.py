#GitHub: github.com/paixaoalmeida
#Projeto de bruteforce de diretórios web
#Hoje em dia é muito difícil não ter um site totalmente blindado contra isso, mas ainda existem excessões
#Inicio: 21 | irei atualizar e deixar melhor
#----------------------------------------------------------------------------------------------------------------
#VARIÁVEIS
import requests
import sys

url = sys.argv[1]
txt = open("listadiretorios.txt")
#----------------------------------------------------------------------------------------------------------------
#Código do programa

for linhas in txt:
    request = requests.get(url+linhas)
    response = request.status_code
    if response == 200 or response == 401:
        print(f"URL:{url+linhas} | STATUS:{response}")







