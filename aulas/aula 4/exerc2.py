rodas = int(input("quantas rodas o veiculo tem ? "))
if(rodas == 4):
    print ("o veiculo é um carro ")
elif(rodas == 2) :
    print ("o veiculo é uma moto ou bicicleta")
elif(rodas == 1):
    print ("o veiculo é um monociclo")
elif(rodas == 6 ):
    print ("o veiculo é um onibus")
elif (rodas >=8 and rodas <=20 ):
    print("o veiculo provavelmente é um caminhão")
else:
    print("nao consegui identificar o tipo de veiculo ")