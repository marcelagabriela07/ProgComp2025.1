
# Faça um programa que tem que adivinhar o número de 1 a 100.
import random

# Faça que essa função gere um número aleatório e a pessoa precisa adivinhar.
print("Você tem que descobrir o número secreto que eu escondo...")

menor = 1
maior = 100
secreto = random.randint(menor, maior)

# Agora vamos começar com 4 tentativas.
tentativas = 1

# Se o palpite for maior que o número secreto o comando avisará.
# Se o palpite for menor que o número secreto o comando avisará.
# Se a pessoa errar o palpite o comando mesmo vai pedir outro palpite até chegar nas 4 tentativas.
# Caso a pessoa acerte o número secreto entre as 4 tentativas, ele vence e não gera mais tentativas.

palpite = int(input("Tentativa 1 - Escolha entre " + str(menor) + " e " + str(maior) + ": "))

if palpite == secreto:
    print("Parabéns! Você acertou", secreto)
else:
    if palpite > secreto:
        print("O número sorteado é menor que", palpite)
        maior = palpite
    else:
        print("O número sorteado é maior que", palpite)
        menor = palpite

    tentativas = tentativas + 1
    palpite = int(input("Tentativa 2 - Escolha entre " + str(menor) + " e " + str(maior) + ": "))

    if palpite == secreto:
        print("Parabéns! Você acertou", secreto)
    else:
        if palpite > secreto:
            print("O número sorteado é menor que", palpite)
            maior = palpite
        else:
            print("O número sorteado é maior que", palpite)
            menor = palpite

        tentativas = tentativas + 1
        palpite = int(input("Tentativa 3 - Escolha entre " + str(menor) + " e " + str(maior) + ": "))

        if palpite == secreto:
            print("Parabéns! Você acertou", secreto)
        else:
            if palpite > secreto:
                print("O número sorteado é menor que", palpite)
                maior = palpite
            else:
                print("O número sorteado é maior que", palpite)
                menor = palpite

            tentativas = tentativas + 1
            palpite = int(input("Tentativa 4 - Escolha entre " + str(menor) + " e " + str(maior) + ": "))

            if palpite == secreto:
                print("Parabéns! Você acertou", secreto)  # Se digitar o número secreto, venceu.
            else:
                print("Você não acertou. O número era:", secreto)  # Se errar, o comando revela o número secreto.