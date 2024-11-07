attack =["Choque do Trovão","Calda de Ferro","Ataque rápido","Esquiva"]
learn = ["Thunder", "Mega Kick", "Mega Punch", "Light"]

print("Seu Pikachu possui os seguintes Golpes: ",attack, "gostaria de aprender um golpe novo ? ")
aprender = str(input( "Sim ou não?"))
if aprender ==("sim"):
    print(attack,"Escolha um golpe pra remover")
    remove=input().lower()
    attack.remove(remove)
    print ("escolha um golpe para aprender",learn)
    learn=input().lower()
    attack.append(learn)
    print("seu set de habilidades é ",attack)
else:
    print("nao aprendeu um golpe novo") 