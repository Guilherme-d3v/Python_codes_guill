# Recebendo variavel para verificação
num = float ( input ( "entre com o número " ) )

# Declarando condições 
if  ( num % 3 == 0 and num % 5 > 0):
    print ( "o número é divisivel por 3 ")

elif  ( num % 5 == 0 and num % 3 > 0):
    print ("o número é divisivel por 5 ")

elif  ( num % 5 == 0 and num % 3 == 0):
    print ("o número é divisivel por 3 e 5 ")

else :
    print ("o número nao é divisivel por 3 nem por 5 ")