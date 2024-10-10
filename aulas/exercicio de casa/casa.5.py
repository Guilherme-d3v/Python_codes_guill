print("Olá seja bem vindo ao nosso Programa de reciclagem") #boas vindas

#corpo de variaveis
papel = "azul"
plastico = "vermelha"
vidro = "verde"
metal = "amarela"
organico = "marrom"
nao_reciclavel = "cinza"
contadorpapel = 0
contadorplastico = 0
contadorvidro = 0
contadormetal = 0
contadororganico = 0
contadornao_reciclavel = 0
decisao = "sim"

while (decisao =="sim"):

    material = int(input("Diga qual categoria de material deseja inserir\n1- papel\n2- plastico\n3- vidro\n4- metal\n5- organico\n6- nao reciclavel  ")) #recebendo material 
    if (material ==1 ): #se adicioonar papel 
        contadorpapel +=1
        decisao = (input("prosseguir com  reciclagem, sim ou nao ?")).lower

    elif (material ==2 ): #se adicioonar plastico   
        contadorplastico +=1
        decisao = (input("prosseguir com  reciclagem, sim ou nao ?")).lower

    elif (material == 3): #se adicioonar vidro    
        contadorvidro +=1
        decisao = (input("prosseguir com  reciclagem, sim ou nao ?")).lower

    elif (material ==4 ): #se adicioonar metal    
        contadormetal +=1
        decisao = (input("prosseguir com  reciclagem, sim ou nao ?")).lower

    elif (material ==5): #se adicioonar organico  
        contadororganico +=1
        decisao = (input("prosseguir com  reciclagem, sim ou nao ?")).lower

    elif (material ==6 ): #se adicioonar nao reciclavel  
        contadornao_reciclavel +=1
        decisao = (input("prosseguir com  reciclagem, sim ou nao ?")).lower


print(f"Voce adicionou\npapel- cor de lixeira {papel} / contagem de elementos {contadorpapel}\nplastico- cor de lixeira {plastico} / contagem de elementos {contadorplastico}\nvidro- cor de lixeira {vidro} / contagem de elementos {contadorvidro}\nmetal- cor de lixeira {metal} / contagem de elementos {contadormetal}\norganico- cor de lixeira {organico} / contagem de elementos {contadororganico}\nnao reciclaveis- cor de lixeira {nao_reciclavel} / contagem de elementos {contadornao_reciclavel}\n")   