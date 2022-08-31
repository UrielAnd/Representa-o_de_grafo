from datetime import datetime
from arq import Arq
from time import sleep

def UI (escolha):       #Interface com o usuário para que escolha entre as opções
    match escolha:
        case "1":
            print("O grau de entrada dessa vertice é: ",arq.predecessores(escolha,numUser))
            sleep(1.5)
        case "2":
            print("O grau de saida dessa vertice é: ",arq.sucessores(escolha,numUser))
            sleep(1.5)
        case "3":
            print("---------------------------------------------------")
            print("Esses são os sucessores de",numUser)
            arq.sucessores(escolha,numUser)
            print("---------------------------------------------------")
            sleep(1.5)
        case "4":
            print("---------------------------------------------------")
            print("Esses são os predecessores de",numUser)
            arq.predecessores(escolha,numUser)
            print("---------------------------------------------------")
            sleep(1.5)
        case "0":
            print("Saindo...")
            exit()
        case _:
            print("ERRO OPÇÃO INVÁLIA")
            sleep(1.5)

nomearq = input("Qual o nome do arquivo e sua extenção?\n|EX: teste.txt|\n= ")      #Entrada do arquivo.txt
numUser = input("Qual n° do vertice?\n= ")                                  #Entrada do vertice
arq = Arq(nomearq)
while True:
    escolha = input("Oque deseja descobrir sobre esse vertice?\n|Grau de entrada -> 1|\n|Grau de saida -> 2|\n|Sucessores -> 3|\n|Predecessores -> 4|\n|Sair -> 0|\n= ")
    UI(escolha)
        