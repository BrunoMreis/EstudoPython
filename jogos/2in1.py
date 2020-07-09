import adivinhacao
import outro_jogo

def execulta():
    print("****************************")
    print("*****Bem Vindo ao 2in1******")
    print("****************************")


    print("Escolha um Jogo!")
    print("(1) Outro Jogo (2) Adivinhação")

    jogo = int(input("Digite número do Jogo: "))

    if(jogo== 1):
        outro_jogo.execulta()
    elif (jogo == 2):
        adivinhacao.execulta()

if(__name__ == "__main__"):
    execulta()