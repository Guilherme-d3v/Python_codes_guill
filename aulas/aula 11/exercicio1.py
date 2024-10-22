import random
mochila =['espada','escudo','poçao']
tem_arco = 'arco' in mochila
tem_espada = "espada" in mochila
escolha=str(input("Ao longo da estrada voce acaba de encotrar um Arco, gostaria de adicionalo ao inventario ? sim ou não ? "))
if (escolha) == "sim" :
    print("sua mochila só possui 3 slots, para pegar o arco voce precisa escolher um item para descartar ",mochila)
    remove=input()
    mochila.remove(remove)
    mochila.append('arco')
    print("voce removeu o seguinte item ",(remove),"voce adicionou o seguinte item (arco)")
    print(mochila)
else:
    print("Voce seguiu seu caminho. sua mochilha contem ", mochila)
print('Ao prosseguir seu caminho voce se deparou com um bandido armado que exige suas poçoes voce tem sua opçao de lutar ou entregar o que ele quer')
decisao=int(input("1-sacar a arma e lutar\n2-luta corporal\n3-entregar\n"))
if decisao == 1:
    if tem_arco or tem_espada in mochila :
        print("Voce defendeu sua honra e seus pertences desse marginal")
    else:
        print("voce lutou sem armas e tomou fumo, FIM DE JOGO ")

elif decisao==2:
    print("voce lutou bravamente mas de forma burra ele estava armado e te matou, FIM DE JOGO ")
elif decisao==3:
    if 'poçao' in mochila:
        mochila.remove('poçao')
        print("voce atendeu a exigencia do bandido")
    else:
        print("o bandido se irritou com a sua mentira e te matou, FIM DE JOGO")