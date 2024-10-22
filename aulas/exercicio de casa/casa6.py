def multiplicar(x,y):
    return x * y 

def dividir (x,y):
    return x/y

def somar(x,y):
    return x + y

def subtrair(x,y):
    return x - y

def potenciar(x,y):
    return pow(x,y)

def divisaoint(x,y):
    return x//y

op=str(input('diga-nos qual operaçao gostaria de efeutar ? multiplicar/dividir/somar/subtrair/potenciar/divisaointeira >>>> '))
n1=float(input('Qual o primeiro termo ? >>>> '))
n2=float(input("Qual o segundo termo ? >>>> "))
if op == 'potenciar':
    produto=potenciar(n1,n2)
    print(produto)

elif op == 'subtrair':
    produto=subtrair(n1,n2)
    print(produto)

elif op == 'somar':
    produto=somar(n1,n2)
    print(produto)

elif op == 'dividir':
    produto=dividir(n1,n2)
    print(produto)

elif op == 'multiplicar':
    produto=multiplicar(n1,n2)
    print(produto)
elif op == 'divisaointeira':
    produto=divisaoint(n1,n2)
    print(produto)
else:
    print("Error")