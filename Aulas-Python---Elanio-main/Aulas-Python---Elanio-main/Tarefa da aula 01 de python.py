
#import sys

# Forumlas 
# P= V* I
# P = R*i**2
# P = v**2 / r

# onde P = corrente , V = tensao, I = corrente , r= resistencia




def calcular_Potencia():
    if(variavel_um == 'V' and variavel_dois == 'i' or (variavel_um == 'i' and variavel_dois == 'V')):
        
        P = valor_V*valor_I
        print('A potencia e de {} Watts, utilizando a formula P= V* I.'.format(P))

    elif(variavel_um == 'R' and variavel_dois == 'i' or (variavel_um == 'i' and variavel_dois == 'R')):

        P =valor_R*valor_I*2
        print('A potencia e de {} Watts, utilizando a formula P = R*i**2 '.format(P))
    elif(variavel_um == 'R' and variavel_dois == 'V' or (variavel_um == 'V' and variavel_dois == 'R')):

        P = valor_V**2/valor_R
        print('A potencia e de {} Watts, utilizando a formula P = v**2 / r. '.format(P))


print('***********************************')
print('**Calculador de potencia em Watts**')
print('***********************************')

print('Primeiramente, iforme dois tipos dados que voce gostaria de usar para o calculo da potencia: ')

variavel_um = str (input('Tipo de dado 1 :(V) Para tensao; (i) Para corrente, (R) Para resistencia.' ))
variavel_dois = input('Tipo de dado 2 :(V) Para tensao; (i) Para corrente, (R) Para resistencia.' )


if ((variavel_um == 'V' or variavel_um == 'v') and (variavel_dois == 'i' or variavel_dois == 'I') or ((variavel_um == 'i' or variavel_um == 'I') and (variavel_dois == 'V' or variavel_um == 'v'))):

    valor_V = (input('Digite o valor da tensao V: '))
    if (valor_V != int ):
        print('Not a number.')
        sys.exit()

    valor_I = (input('Digite o valor da corrente i: '))
    if (valor_I != int ):
        print('Not a number.')
        sys.exit()

    if (valor_V and valor_I == 0):
        print('Nao e possivel calcular a potencia.')       
    else:
        calcular_Potencia()

elif((variavel_um == 'R'or variavel_um == 'r') and (variavel_dois == 'i' or variavel_dois == 'I') or ((variavel_um == 'I'or variavel_um == 'i') and (variavel_dois == 'R' or variavel_dois == 'r'))):

    valor_R = (input('Digite o valor da resistencia: '))
    if (valor_R != int ):
        print('Not a number.')
        sys.exit()

    valor_I = (input('Digite o valor da corrente: '))
    if (valor_I != int ):
        print('Not a number.')
        sys.exit()
    
    if (valor_R and valor_I == 0):
        print('Nao e possivel calcular a potencia.')
    elif ( isinstance(valor_I, str) or (valor_R, str) ):
        print('Not a number.')
    else:
        calcular_Potencia()

elif ((variavel_um == 'R' or variavel_um == 'r') and (variavel_dois == 'V' or variavel_dois == 'v') or ((variavel_um == 'V' or variavel_um == 'v') and (variavel_dois == 'R' or variavel_dois == 'r') )):

    valor_V = (input('Digite o valor da tensao: '))
    if (valor_V != int ):
        print('Not a number.')
        sys.exit()

    valor_R = (input('Digite o valor da resistencia: '))

    if (valor_R != int ):
        print('Not a number.')
        sys.exit()

    if (valor_V and valor_R == 0):
        print('Nao e possivel calcular.')
    elif ( isinstance(valor_R, str) or (valor_V, str) ):
        print('Not a number.')
    else: 
        calcular_Potencia()
