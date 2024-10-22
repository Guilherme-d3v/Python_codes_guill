#função : calculadora de quadrado de um numero 
def quadrado (calc):
    return calc **2

numero = float(input("digite um numero "))
resultado = quadrado(numero) #recebe o retorno da funçao 
print(f"o quadrado de {numero} é {resultado}")
