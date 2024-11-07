print ("Olá,Seja bem vindo a nossa lanchonete")
item1 = "Hamburguer"
item2 = "batata frita"
item3 = "refrigerante"
item4 = "combo"
primeiro = int ( input (f"você gostaria de escolher produtos individualmente ou optar pelo combo ? \n 1 - escolher produto \n 2- Combo ")) #decisao de combo ou escolha
if primeiro == 2: #caso seja combo
    valortotal = 22
    print(f"pedido concluido com sucesso. Voce optou por {item4}  no valor de {valortotal} reais ")
elif primeiro == 1: #caso seja escolha
    pedido1 = int(input(" 1- Hamburguer\n 2- Batata frita\n 3- refrigerante ")) #escolhendo o primeiro item do pedido
    if pedido1 == 1: #caso seja hamburguer o primeiro pedido
        valortotal=10
        adicional = int(input("Gostaria de adicionar mais itens ?\n 1- sim\n 2- nao ")) #adicionando ao pedido
        if (adicional) == 2 : #caso nao haja adicional
            print(f"pedido concluido com sucesso. Voce optou por {item1}  no valor de {valortotal} reais") #devolvendo pedido finalizado
        elif adicional == 1: #caso haja adicional no pedido
            segundo=int(input("adicione...\n 1- Batata frita\n 2- refrigerante ")) #escolhendo o segundo item do pedido        
            if segundo ==1: #se for batata frita
                valortotal=valortotal+10
                conclusao = int(input("Por mais 2 reais gostaria de fechar o combo completo ?\n 1- sim\n 2- nao "))
                if conclusao==1: #caso haja o combo
                    valortotal=valortotal+2 
                    print (f"pedido concluido comsucesso voce optou por {item4} no valor total {valortotal} ")
                elif conclusao==2:  #caso nao haja o combo 
                    print(f"pedido concluido com sucesso voce optou por {item1} e {item2} no valor de {valortotal}")
            elif segundo ==2: #se for refrigerante
                valortotal=valortotal+10
                conclusao = int(input("Por mais 2 reais gostaria de fechar o combo completo ?\n 1- sim\n 2- nao "))
                if conclusao==1: #caso haja o combo
                    valortotal=valortotal+2 
                    print (f"pedido concluido comsucesso voce optou por {item4} no valor total {valortotal} ")
                elif conclusao==2:  #caso nao haja o combo 
                    print(f"pedido concluido com sucesso voce optou por {item1} e {item3} no valor de {valortotal}")
    elif pedido1 == 2: #caso seja batata o primeiro pedido
        valortotal=10
        adicional = int(input("Gostaria de adicionar mais itens ?\n 1- sim\n 2- nao ")) #adicionando ao pedido
        if (adicional) == 2 : #caso nao haja adicional
            print(f"pedido concluido com sucesso. Voce optou por {item2}  no valor de {valortotal} reais") #devolvendo pedido finalizado
        elif adicional == 1: #caso haja adicional no pedido
            segundo=int(input("adicione...\n 1- Hamburguer\n 2- refrigerante ")) #escolhendo o segundo item do pedido    
            if segundo ==1: #se for Hamburguer
                valortotal=valortotal+10
                conclusao = int(input("Por mais 2 reais gostaria de fechar o combo completo ?\n 1- sim\n 2- nao ")) #perguntando se tem combo 
                if conclusao==1: #caso haja o combo
                    valortotal=valortotal+2 
                    print (f"pedido concluido comsucesso voce optou por {item4} no valor total {valortotal} ")
                elif conclusao==2:  #caso nao haja o combo 
                    print(f"pedido concluido com sucesso voce optou por {item2} e {item1} no valor de {valortotal}")
            elif segundo ==2: #se for refrigerante
                valortotal=valortotal+10
                conclusao = int(input("Por mais 2 reais gostaria de fechar o combo completo ?\n 1- sim\n 2- nao "))
                if conclusao==1: #caso haja o combo
                    valortotal=valortotal+2 
                    print (f"pedido concluido comsucesso voce optou por {item4} no valor total {valortotal} ")
                elif conclusao==2:  #caso nao haja o combo 
                    print(f"pedido concluido com sucesso voce optou por {item2} e {item3} no valor de {valortotal}")
    elif pedido1 == 3: #caso seja refrigerante o primeiro pedido
        valortotal=10
        adicional = int(input("Gostaria de adicionar mais itens ?\n 1- sim\n 2- nao ")) #adicionando ao pedido
        if (adicional) == 2 : #caso nao haja adicional
            print(f"pedido concluido com sucesso. Voce optou por {item3}  no valor de {valortotal} reais") #devolvendo pedido finalizado
        elif adicional == 1: #caso haja adicional no pedido
            segundo=int(input("adicione...\n 1- Hamburguer\n 2- batata frita ")) #escolhendo o segundo item do pedido    
            if segundo ==1: #se for Hamburguer
                valortotal=valortotal+10
                conclusao = int(input("Por mais 2 reais gostaria de fechar o combo completo ?\n 1- sim\n 2- nao ")) #perguntando se tem combo 
                if conclusao==1: #caso haja o combo
                    valortotal=valortotal+2 
                    print (f"pedido concluido comsucesso voce optou por {item4} no valor total {valortotal} ")
                elif conclusao==2:  #caso nao haja o combo 
                    print(f"pedido concluido com sucesso voce optou por {item3} e {item1} no valor de {valortotal}")
            elif segundo ==2: #se for hamburguer
                valortotal=valortotal+10
                conclusao = int(input("Por mais 2 reais gostaria de fechar o combo completo ?\n 1- sim\n 2- nao "))
                if conclusao==1: #caso haja o combo
                    valortotal=valortotal+2 
                    print (f"pedido concluido comsucesso voce optou por {item4} no valor total {valortotal} ")
                elif conclusao==2:  #caso nao haja o combo 
                    print(f"pedido concluido com sucesso voce optou por {item3} e {item2} no valor de {valortotal}")