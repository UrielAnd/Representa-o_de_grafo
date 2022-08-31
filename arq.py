from time import sleep

class Arq:
    def __init__ (self, nomearq):
        try:
            self.arquivo = open(nomearq,"r")
            self.lista_Arq = (self.arquivo.readlines()) #Lê do arquivo para uma lista
        except Exception as error:
            print(error)
            exit()
    
    #SUCESSORES + GRAU DE SAÍDA DO VALOR INFORMADO PELO USUÁRIO    
    def sucessores(self,escolha,numUser):
        cont = 0        #Conta graus
        hp = 0
        #print (self.lista_Arq)
        for i in self.lista_Arq:
            #print(i)
            i = i.strip("\n")
            listsplit=(i.split(" "))        #Split dos espasos vazios
            #listsplit.remove("")
            listfilter = list(filter(("").__ne__, listsplit)) #A função filter() assume outra função, __ne__, que retornará um bool True ou False com base no fato de o valor 1 estar presente na lista myList ou não. Se o valor 1 estiver presente na lista, ele simplesmente o descartará. Então, tudo o que for retornado pela função filter() será convertido em uma lista usando a função list().
            #print(listsplit)
            #print (listfilter)
            #for i in range(len(listsplit)):
                #print(i)
                #sleep(2)
                #if listsplit[i-1] == "":
                    #listsplit.__delitem__(int(i)-1)
                    #print(listsplit)
                    #if len(listsplit)==2:
                        #break
                    #print("teste")
            #print(listfilter)
            #print(len(listsplit))
            #print(numUser)
            if hp == 1:
                if listfilter[0] == str(numUser):
                    if escolha == "3":
                        print(listfilter[1])  #printa as respostas
                    cont += 1
            hp=1
        return cont

    #PREDECESSORES + GRAU DE ENTRADA DO VALOR INFORMADO PELO USUÁRIO 
    def predecessores(self,escolha,numUser):
        cont = 0        #Conta grau
        hp=0
        #print (self.lista_Arq)
        for i in self.lista_Arq:
            #print(i)
            i = i.strip("\n")
            listsplit=(i.split(" "))        #Split dos espasos vazios
            #listsplit.remove("")
            listfilter = list(filter(("").__ne__, listsplit))   #A função filter() assume outra função, __ne__, que retornará um bool True ou False com base no fato de o valor 1 estar presente na lista myList ou não. Se o valor 1 estiver presente na lista, ele simplesmente o descartará. Então, tudo o que for retornado pela função filter() será convertido em uma lista usando a função list().
            #print(len(listsplit))
            #sleep(0.5)
            #print(listfilter)
            #print(listsplit)
            #print(numUser)
            if hp == 1:   
                if listfilter[1] == str(numUser):
                    if escolha == "4":
                        print(listfilter[0])  #printa as respostas
                    cont += 1                    
            hp=1
        return cont