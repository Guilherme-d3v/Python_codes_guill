
x = True
soma = 0 
entrada = 0
saida = 0
while (x==True):
    entrada = float(input("Entre com o valor "))
    soma += entrada
    print (soma)
    keep = str(input("continuar sim ou nao?"))
    if keep != "sim":
        print(f"a soma total é {soma}")
    else:
        (x==False)