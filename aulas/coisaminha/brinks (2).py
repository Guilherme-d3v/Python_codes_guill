import random
import time

personagem = [
    ['HP','ATK','DEF'],
    [100,20,20]
]
#hpp1=personagem[1][0]
#atkp1=personagem[1][1]
#defp1=personagem[1][2]
maquina = [
    ['HP','ATK','DEF'],
    [100,20,20]
]
#hppc=maquina[1][0]
#atkpc=maquina[1][1]
#defpc=maquina[1][2]



fight=str(input("voce está pronto para a batalha ?\n "))

if fight == 'sim':
    while personagem[1][0] > 0 and maquina[1][0] > 0:
        rollp1=random.randint(1,6)
        rollpc=random.randint(1,6)
        danop1=personagem[1][1]*(rollp1/2)-maquina[1][2]
        danopc=maquina[1][1]*(rollpc/2)-personagem[1][2]
        maquina[1][0]=maquina[1][0]-danop1
        print('voce atacou e diminuiu o hp do oponente para ',maquina[1][0])
        personagem[1][0]=personagem[1][0]-danopc
        print('o oponente atacou e diminuiu seu hp para ',personagem[1][0])

    if personagem[1][0]>maquina[1][0]:
            print('voce venceu ! seus pontos de vida ',personagem[1][0],' pontos de vida do seu oponente',maquina[1][0])
    elif personagem[1][0]<maquina[1][0]:
            print('voce perdeu ! seus pontos de vida', personagem[1][0],'pontos de vida do seu oponente',maquina[1][0])
else:
    print("voce fugiu...")    