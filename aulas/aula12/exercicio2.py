import time
status=[100, 20]
contador= 7

print(f'seu poder de ataque é',status[1] )
print(f'seu HP maximo é',status[0] )

while status[1] <=30:
    train=str(input("Gostaria de treinar? "))
    if train =='sim':  
        status[1]+=1
    elif train == "nao":
        print('voce encerrou seu treinamento seus stats ficarma em', status)
    while contador > 0:
        print(contador)
        time.sleep(1)
        contador -= 1
        time.sleep(1)
        print("training...")
    contador = 7
    print("treinamento concluido")   
    print(f'Seus pontos de força subiram para',status[1])
    
else:
    print("Voce atingiu o limite de treino")