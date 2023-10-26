import forca
import adivinhaçãoFor

print('Escolha o seu jogo!')
print('(1) Jogo da forca\n(2) Jogo de adivinhação')

userChoice = int(input('Qual será o jogo ?'))

if (userChoice == 1):
    print('Jogando Forca!')
    forca.jogar()
elif (userChoice == 2):
    print('Jogando adivinhação!')
    adivinhaçãoFor.jogar()

    
