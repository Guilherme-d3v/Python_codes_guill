#programa que pergunta o nome do cliente, o modelo do carro e sua cor e imprime uma mensagem agradecendo a preferencia com as informaçoes solicitadas na mensagem 
nome_do_cliente = input("Qual seu nome? ")
modelo_do_carro = input("Qual modelo do seu carro ? ")
Cor = input("Qual a cor do seu carro ? ")
print(nome_do_cliente+",","agradecemos pela preferencia e gostariamos que soubesse que sempre estamos a disposiçao para cuidar do seu",modelo_do_carro,Cor)
print("Qual dia você gostaria de agendar a lavagem do",modelo_do_carro,Cor, "? hoje ou amanhã?")
dia_de_lavagem = input()
print("O Agendamento para lavagem do seu",modelo_do_carro,Cor,"está concluida para o dia de",dia_de_lavagem)