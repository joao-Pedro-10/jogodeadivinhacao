import random
print("#######################")
print("#                jogo da adivinhação #                       ")
print("# 🔥                JOAO    🔥   #                           ")
print("# 🔥                PEDRO   🔥                               ")
print("#      # #     #  # #    #  #      #  #      #  # # #         ")
print("#      #   #   #  # #    #    #    #    #    #      #         ")
print("#      #  #    #         #    #    #  #      #      #         ")          
print("#      #       #  # #    #   #     #    #    #  # # #         ")
print("#######################")
numeroSecreto = random.randrange(0,100)
totalTemtativas = 0
pontos = 100

print("Qual nivel de dificuldade? ")
print("(1)- Fácil (2)- medio (3)- dificil")

nivel = int(input("Escolha um nivel"))

if nivel == 1:
    print("você escolheu o nivel facíl, você é fraco ainda !")
    print(" você tem 20 tentativas não quer ir no mais dificil beta ? ")
elif nivel == 2:
    print("voce escolheu o nivel médil até que enfim você criou coragem !")
    print(" você tem 10 tentativas apenas, use com responsabilidade !")
elif nivel == 3:
    print("voce escolheu o nivel dificil,parabéns guerreiro !")
    print(" voce tem apenas 5 tentativas, vc tem coragem !")
    totalTentativas = 5


for rodada in range (1, totalTentativas +1): 
    print("Tentativa {} de {}".format(rodada,totalTentativas) )
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or > 100):
        print("Número invaledo desculpe")
        continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto 

    if(acertou):
        print(f"Você acertou e fez {pontos}parabéns! ")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")

            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

print("Fim de jogo ! O número era ",numeroSecreto)
