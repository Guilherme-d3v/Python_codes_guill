escolha = int(input("Olá bem vindo ao nosso lava a jato, escolha sua opçao de lavagem\n 1- Lavagem completa R$50,00\n 2- Lavagem basica R$ 35,00\n"))
pretinho = int(input ("por mais 5 reais gostaria de adicionar pretinho?\n 1- sim\n 2- nao\n"))
if (escolha == 1 and pretinho == 1):
    print ("voce optou por lavagem Completa com aplicação de pretinho no valor de R$ 55,00 reais")
elif escolha ==1 and pretinho ==2:
    print ("voce optou por lavagem Completa sem a aplicação de pretinho no valor de R$ 50,00 reais")
elif escolha ==2 and pretinho ==1:
    print ("voce optou por lavagem basica com aplicação de pretinho no valor de R$ 40,00 reais")
elif escolha == 2 and pretinho == 2:
    print ("voce optou por lavagem basica sem aplicação de pretinho no valor de R$ 35,00 reais")
