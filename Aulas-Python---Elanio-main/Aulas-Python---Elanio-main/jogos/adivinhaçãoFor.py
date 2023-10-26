
def jogar():

    import random

    print('Jogo da adivinhação utilizando for loops! \n\n')
    dificuldade = int(input('Por favor, escolha sua dificuldade!\n(1) - Facil\n(2) - Medio\n(3) - Dificil\nDigite aqui:\n'))
    print('\n')

    totalTentativa = 0

    if (dificuldade == 1):
        totalTentativa = 15
    elif (dificuldade == 2):
        totalTentativa = 10
    elif (dificuldade == 3):
        totalTentativa = 5

    numeroSecreto = random.randint(1,50)


    # O loop for ja incrementa automaticamente o valor de numeroTentativa.

    for numeroTentativa in range (1,totalTentativa + 1):

        print(f'Tentativa {numeroTentativa} de {totalTentativa}')
        userInput = int(input('Digite seu numero!\n'))

        if (userInput < 0):
            print('Numero Invalido!')
            continue

        if (userInput == numeroSecreto):
            print('Parabens voce acertou!\n')
            break

        elif (userInput > numeroSecreto):
            print('Numero maior do que o numero secreto!\n')
            continue

        elif(userInput < numeroSecreto):
            print('Numero menor do que o numero secreto!\n')
            continue

    print(f'O numero era {numeroSecreto}!')
    print('Suas tentativas acabaram!\n')
    print('############')
    print('Fim de jogo!')
    print('############\n\n')
        


if (__name__ == '__main__'): 
    #Verifica se o arquivo esta sendo executado diretamente ou se esta sendo importado.
    #Se o arquivo for executado diretamente de adivinhaçãoFor.py, a condição será TRUE, mas se for executado pelos jogos.py, a condição sera FALSE.

    jogar()
        
