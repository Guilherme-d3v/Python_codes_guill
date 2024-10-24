import time
aventureiro = [
    ["Vida", "Ataque"],
    [100, 20]
]
assaltante = [
    ["Vida", "Ataque"],
    [60, 20]
]
vidaav = aventureiro[1][0]
vidaas = assaltante[1][0]
atakav=aventureiro[0][1]
atakas=assaltante[0][1]
print(vidaav)
print("Ao seguir seu caminho voce encontrou outro asssaltante, ele nao tem interesse em pertences, e parte para a batalha ")
while vidaas and vidaav > 0:
    vidaav-=assaltante[1][1]
    vidaas-=aventureiro[1][1]
    time.sleep(1)
    print(f"sua vida {vidaav}")
    print(f"vida do seu oponente {vidaas}")

if vidaav <=0:
   print('fim de batalha o oponente vence')
elif vidaas <=0:
    print('fim de batalha voce venceu')

