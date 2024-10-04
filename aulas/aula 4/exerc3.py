peso = float (input("Olá, diga-nos seu peso "))
altura = float( input("agora, diga-nos sua altura "))
imc = (peso/(altura*altura))

if (imc < 18.5):
    print ("magreza")

elif (imc >= 18.5 and imc <= 24.9):
    print(f"seu imc é {imc:.2f} classificado como normal")

elif (imc >24.9 and imc <= 29.9):
     print (f"seu imc é {imc:.2f} classificado como sobrepeso")

elif (imc >29.9 and imc <=39.9):
    print (f"seu imc é {imc:.2f} classificado como obesidade ")

elif (imc >40):
    print(f"seu imc é {imc:.2f} classificado como obesidade grave")

else:
    print("que que ta acontecendo aqui gente ????")