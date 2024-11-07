import random

n1 = random.uniform (1,15)
n2 = random.uniform (1,15)
n3 = random.uniform (1,15)
#print (f"{n1} {n2} {n3}")
escolha = int(input("o sistem gerou 3 numeros qual voce acha que é o maior ? "))

if escolha == 1 and n1>n2 and n1>n3:
    print ("voce acertou ")
elif escolha == 2 and n2>n1 and n2>n3:
    print ("voce acertou")
elif escolha == 3 and n3>n2 and n3>n1:
    print ("voce acertou")
else:
    print("voce errou")    