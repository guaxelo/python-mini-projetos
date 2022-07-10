from random import randint


def numero_robo():
    escolhaNumero_robo = randint(1, 100)
    return escolhaNumero_robo

def numero_jogador():
    escolhaNumero_jogador = int

    while vidas:
        try:
            escolhaNumero_jogador = int(input('Qual numero voce acha que o robo vai escolher? '))
        except ValueError:
            print("Não é número")

        if type(escolhaNumero_jogador) == int:
            break

    return escolhaNumero_jogador


print('==================== JOGO DE ADIVINHAÇÃO ====================\n')

vidas = 7
jogador = 0
robo = numero_robo()
ganhou = False

while vidas:

    print(f'>> VIDAS {vidas}')
    print(f'>> SEU NUMERO ANTERIOR: {jogador}')
    jogador = numero_jogador()



    if robo == jogador:
        ganhou = True
    elif robo > jogador:
        print('=============================== \nESCOLHA UM NUMERO MAIOR! \n===============================')
    else:
        print('=============================== \nESCOLHA UM NUMERO MENOR! \n===============================')

    if ganhou == True:
        break
    elif vidas == 0:
        break
    else:
        vidas -= 1


if vidas == 0:
    print('VOCE PERDEU!')
    print(f'>> NUMERO DO ADVERSARIO {robo}')
elif ganhou == True:
    print('PARABENS, VOCE VENCEU!')
