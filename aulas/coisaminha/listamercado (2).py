mercado=[]
carrinho=[]
menu='lista'

while menu == 'lista' or menu == 'carrinho':
    menu=str(input("Gostaria de adicionar itens a lista ou ao carrinho "))
    if menu == "lista":
        item=(input("adicione o item "))
        mercado.append (item)
        print(mercado)
    elif menu == "carrinho":
        remove=(input("adicione o item ao carrinho"))
        carrinho.append(remove)
        if remove in mercado:
            mercado.remove(remove)
        print(carrinho)
    else:
        print("nao entendemos sua escolha")
        menu='lista'