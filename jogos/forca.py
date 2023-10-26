def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "bana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        index = 0
        if (chute in palavra_secreta):

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index+= 1

        else:
            erros+= 1

        acertou = '_' not in letras_acertadas
        enforcou == erros == 6


    if (acertou):
        print('Voce Ganhou!')
    else:
        print('Voce perdeu!')

          



        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
