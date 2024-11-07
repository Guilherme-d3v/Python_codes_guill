mochila = ['poçao','escudo','espada']

print('Ao prosseguir seu caminho voce se deparou com um bandido armado que exige suas poçoes voce tem sua opçao de lutar ou entregar o que ele quer')
decisao=int(input("1-sacar a espada e lutar\n2-luta corporal\n3-entregar\n"))
if decisao == 1:
    if 'espada' in mochila:
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
else:
    print("o bandido se aproveitou de sua distraçao e te atacou, FIM DE JOGO")