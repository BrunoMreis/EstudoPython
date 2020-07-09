
import random


def execulta():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")      

    numero_secreto = random.randrange(1, 101)
    numero_de_tentativa = 3
    rodada = 1
    pontos = 1000

    print("Dificulade do jogo 1 -> Fácil, 2-> Médio, 3-> Difícel")
    dificuldade = int(input("Digite nível da dificuldade: "))

    if(dificuldade == 1):
        numero_de_tentativa = 20
    elif(dificuldade == 2):
        numero_de_tentativa = 10
    else:
        numero_de_tentativa = 5

    for rodada in range(1, numero_de_tentativa + 1):
        print("Tentativa {} de {}! ".format(rodada, numero_de_tentativa))
        chute = int(input("Digite um numero entre 1 e 100: "))
        if(chute < 1 or chute > 100):
            print("Você digitou um número inválido! ")
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou com {} pontos!".format(pontos))

            break
        else:
            perdidos = abs(chute - numero_secreto)
            pontos = pontos - perdidos
            if(numero_de_tentativa == rodada):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
            elif(maior):
                print("Você informou um numero maior ")
            elif(menor):
                print("Voce informou um número menor")

    print("*********************************")
    print("Fim do Jogo!")
    print("*********************************")

if(__name__ == "__main__"):
    execulta()