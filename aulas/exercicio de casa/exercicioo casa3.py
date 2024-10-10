print ("Olá,Seja bem vindo a nossa lanchonete")
pedido = int(input ("você gostaria de escolher produtos individualmente ou optar pelo combo ? \n 1 - escolher produto \n 2- Combo\n"))
item1 = "hamburguer"
item2 = "batata frita"
item3 = "refrigerante"
item4 = "combo"

if pedido ==1:  
    print(f"Escolha seus itens\n 1- hamburguer R$10,00\n 2- batata frita R$ 10,00\n refrigerante R$10,00)")
    escolha1 = input()
    valortotal = 10
    if (escolha1) == 1:
    escolha2 =input("Gostaria de adicionar algo ao seu pedido ?\n 1- adicionar itens\n 2- concluir pedido ")
    if escolha2 = 1:
        print(f"Escolha seus itens\n 1- batata frita R$ 10,00\n refrigerante R$10,00")
        escolha2= input()
    if escolha2== 1:
        valortotal =valortotal+10
        print("Voce escolheu até agora {item1} e {item2} por mais 2 reais gostaria de adicionar um refrigerante ?\n 1 - para sim\n 2 - para nao")
        adicional =input()
        if adicional==1:
            valortotal=valortotal+2
            print(f"voce optou pelo {item4} no valor total de {valortotal}")
        elif adicional==2:
            print("seu pedido é {item1} e {item2} no valor total de {valortotal}")   
elif pedido==2:
    valortotal = 22
    print(f"pedido concluido, voce optou por {pedido} no valor total de {valortotal}")
else:
    print("nao conseguimos entender seu pedido. por favor repita o processo se atentando as opçoes.")    