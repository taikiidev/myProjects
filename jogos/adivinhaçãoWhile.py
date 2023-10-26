# Refazendo jogo de advinhação da Alura.
print('\n\n')
print('Bem vindo ao jogo de adivinhação.')
print('Neste jogo voce deve adivinhar o numero secreto!\n')
 
numeroSecreto = 40
totalTentativas = 3
qualTentativa = 1


while (qualTentativa <= totalTentativas) :
    print(f'Tentativa {qualTentativa} de {3}')
    userInput = int(input('Digite seu numero!\n'))

    
    if (userInput == numeroSecreto):
        print('Parabens, voce ganhou!')
        break
        
    elif (userInput > numeroSecreto):
        print('Seu numero e maior do que o numero alvo!\n')
        qualTentativa = qualTentativa + 1

    elif (userInput < numeroSecreto):
        print('Seu numero e menor do que o numero alvo\n')
        qualTentativa = qualTentativa + 1

print('Suas chances acabaram!')
print('Fim de jogo!')