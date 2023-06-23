import time
from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

print(f"""{Fore.LIGHTRED_EX}


░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░  ██╗░░░██╗░░███╗░░
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗  ██║░░░██║░████║░░
╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║  ╚██╗░██╔╝██╔██║░░
░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║  ░╚████╔╝░╚═╝██║░░
██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║  ░░╚██╔╝░░███████╗
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝
                                   


            Bem vindo ao ambiente.

""")

#MENU DO PROJETO
def menu():
    print("1 - Criar arquivo")
    print("2 - Editar programa")
    print("3 - Ver arquivos")
    
    print("4 - Sair do programa")
#CRIAR ARQUIVO    
def criar_arquivo(arquivos):
    teste = input("Qual o nome do arquivo?")
    teste1 = input("Qual o conteudo do texto?")
    teste2 = input(".bat .txt .ipynb .py ou .exe?")
    arquivo = open(f"{teste}.{teste2}", "w")
    arquivo.write(teste1)
    arquivo.close()
    arquivos.append(f"{teste}.{teste2}")
    time.sleep(3)
    print("Arquivo feito com sucesso!")
    time.sleep(5)
#EDITAR ARQUIVO    
def escrever_arquivo(arquivos): 
    if len(arquivos) == 0:
        print("Nenhum arquivo para se alterar")
    else:
        nome = input("Qual o nome do arquivo?")
        final = input(".bat .txt .ipynb .py ou .exe?")
        meio = input("O que voce deseja adicionar ao arquivo?")
    
        arquivo = open(f"{nome}.{final}", "w")
        arquivo.write(meio)
        arquivo.close()
        print("Alterando.")
        time.sleep(1)
        print("Alterando..")
        time.sleep(1)
        print("Alterando...")
        time.sleep(1)
        print("Alterando....")
        time.sleep(1)
        print("Alterado com sucesso")


                
#VER ARQUIVO        
def ver_arquivo(arquivos):
    
    if len(arquivos) == 0:
        print("Nenhum arquivo adicionado!")
    else:
        
        print("---------------")
        for arquivo in arquivos:
            print(arquivo)
        print("---------------")
    
    

#DICIONARIO VAZIO 
arquivos = []

#LOOP MENU  
while True:
    menu()
    opcao = input("Escolha:")
    
    if opcao == '1':
        criar_arquivo(arquivos)
    elif opcao == '2':
        escrever_arquivo(arquivos)
    elif opcao == '3':
        ver_arquivo(arquivos)
    else:
        print("Obrigado por usar nosso sistema!")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("Ate mais!")
        break
