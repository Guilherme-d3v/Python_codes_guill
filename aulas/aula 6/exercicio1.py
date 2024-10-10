soma = 0
contador = 0 

#solicita ao usuario que insira 5 numeros 
while contador <5:
    numero = float(input("Insira um numero "))
    soma += numero
    contador += 1
#exibe soma total
    print(f"a soma total é {soma}")