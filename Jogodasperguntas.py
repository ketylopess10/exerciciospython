pontuacao = 0 

print('Bem-vindo ao Jogo das Perguntas')

#Primeira pergunta
resposta = input('Qual a capital frança?')
if resposta.lower() == 'paris':
    print("Correto!")
    pontuacao += 1
else: 
    print("Errado!")

    #Segunda pergunta 

resposta = input('Qualo maior planeta do sistema solar?')
if resposta.lower() == 'jupiter' or resposta.lower() == 'jupiter':
     print("Correto!")
     pontuacao += 1
else:
     print("Errado!")

     #terceira pergunta
resposta = input('Quanto 5 + 5?')
if resposta.lower() == '10':
    print ("Correto!")
    pontuacao += 1
else:
    print("Errado!")

    print(f"Sua pontuação final é: {pontuacao} de 3 perguntas")
    