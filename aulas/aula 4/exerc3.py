peso = float (input("Olá, diga-nos seu peso "))
altura = float( input("agora, diga-nos sua altura "))
imc = (peso/(altura*altura))
if (imc < 18.5):
    print ("magreza")
elif (imc >= 18.5 and imc <= 24.9):
    print("normal")
elif (imc >24.9 and imc <= 29.9):
     print ("sobrepeso")
elif (imc >29.9 and imc <=39.9):
    print ("obesidade ")
elif (imc >40):
    print("obesidade grave")
else:
    print("que que ta acontecendo aqui gente ????")