import time
print("Olá, seja bem vindo a nossa auto-analise corporal. ")
time.sleep(1)
nome=input("Qual seu nome ? ")
idade=int(input("Qual a sua idade ? "))
celuar=input("Qual seu numero de celular? digite sem traços ou pontos : ")
email=input("Qual seu email? : ")
esquizoide=0
oral=0
mazoquista=0
psicopata=0
rigido=0

formato_rosto=int(input("Qual formato mais se assemelha ao do seu rosto ?\n1- Oval.\n2- Redondo.\n3- Quadrado.\n4- Triangulo invertido.\n5- simetrico (oval proprorcional)\n:"))
if formato_rosto==1:
    esquizoide+=1
elif formato_rosto==2:
    oral+=1
elif formato_rosto==3:
    mazoquista+=1
elif formato_rosto==4:
    psicopata+=1
elif formato_rosto==5:
    rigido+=1
else:
    print("nao entendemos sua resposta")
    
formato_rosto=int(input("Qual formato mais se assemelha ao do seu torax ?\n1- Torax plano,pode apresentar cavidade concava no plexo solar. Transmite pouca força.\n2- Macio e aconchegante, segue a proporçao do quadril. Em geral seios fartos e arredondados em mulheres.\n3- Retangular, musculatura firme, seios fartos e caidos. Projeta os seios para frente.\n4- Torax largo e estufado, a cintura é definida e segue o padrão triangulo invertido.\n5- Torax esguio de aparencia atletica. Em mulheres seios pequenos e firmes.\n:"))
if formato_rosto==1:
    esquizoide+=2
elif formato_rosto==2:
    oral+=2
elif formato_rosto==3:
    mazoquista+=2
elif formato_rosto==4:
    psicopata+=2
elif formato_rosto==5:
    rigido+=2
else:
    print("nao entendemos sua resposta")

# Corrigido: usar sorted() para criar uma lista ordenada
Lista_de_diagnostico = sorted([esquizoide, oral, mazoquista, psicopata, rigido], reverse=False)

traço_dominante1 = Lista_de_diagnostico[-1]  # maior valor
traço_dominante2 = Lista_de_diagnostico[-2]  # segundo maior valor

print(f"Seu traço dominante é ",Lista_de_diagnostico[-1])
print(f"Seu segundo traço dominante é ",Lista_de_diagnostico[-2] )