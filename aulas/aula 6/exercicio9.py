n1=int(input("Digite o primeiro valor "))
n2=int(input("Digite o segundo valor "))
op=int(input("1- somar\n2- subtrair\n3- multiplicar\n4- dividir\n"))1

if (op == 1):
        soma=(n1 + n2)
        print (soma)
elif (op == 2):
    soma=(n1 - n2)
    print(f"{soma}")
elif (op == 3):
    soma=(n1 * n2)
    print(f"{soma}")
elif (op == 4):
    soma=(n1 / n2)
    print(f"{soma}")