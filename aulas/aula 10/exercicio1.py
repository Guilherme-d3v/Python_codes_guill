import random

num1 = random.uniform (1, 15)
num1a = round(num1,2)
num2 = random.uniform (1, 15)
num2a = round(num2,2)
num3 = random.uniform (1, 15)
num3a = round(num3,2)
#print(f"{num1a}\n{num2a}\n{num3a}")
resposta = float(input("Tente adivinhar qual é o maior da sequencia "))
if resposta == num1a or resposta == num2a or resposta ==num3a and resposta >= num3a and resposta >= num2a and resposta >= num1a:
    print("acertou miseravel")
else:
    print("tenteeee outra veeeez ")
