armario = [
    ['',"","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""],
    ["","","","",""]
]
armariovip = [
    ['','',''],
    ['','',''],
    ['','','']
]

nome=input("Olá caro aluno, qual seu nome ? ")
choice=str(input("Escolha seu armario\nvip(3x3) - R$50,00\ncomum(5x5) - R$30,00\n"))

if choice == "vip":
    x=int(input("Qual linha do armario será sua gaveta ? "))
    y=int(input("Qual coluna do armario será sua gaveta ? "))
    armariovip[x][y] = nome
    for x in armariovip:
        print(x)

elif choice == "comum":
    x=int(input("Qual linha do armario será sua gaveta ? "))
    y=int(input("Qual coluna do armario será sua gaveta ? "))
    armario[x][y] = nome
    for x in armario:
        print(x)

else:
    print("Nao conseguimos entender sua escolha, por favor repita o processo")