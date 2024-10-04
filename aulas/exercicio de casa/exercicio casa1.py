#recebendo dados necessarios
aro= int (input ("Olá usuário, diga o tamanho de Aro que deseja comprar para que possamos lhe orientar quanto nos demais periféricos "))
#calculando tamanho de periféricos 
guidao= aro/2
manet=aro/4
quadro = aro
#devolvendo ao usuario as dimensoes calculadas
#print (f"Com base no Aro informado\n O tamanho ideal de guidao é {guidao}\n O tamanho ideal de manet é {manet}\n O tamanho ideal de quadro é {quadro}")
print("como base no Aro informado\n o tamanho ideal de guidao é {}\n o tamnho ideal de manet é {}\n o tamanho idedal de quado é {}".format(guidao,manet,aro))