import random
from collections import OrderedDict

chordList = {
    'cmaj' : 'CEG' ,
    'dmaj' : 'DF#A' ,
    'amaj' : 'AC#E' ,
    'emaj' : 'EG#B' ,
    'fmaj' : 'FAC' ,
    'bmaj' : 'BD#F#',
    'cmaj7': 'CEGA#',
    'dmaj7': 'DF#AC',
    'amaj7': 'AC#EG',
    'emaj7': 'EG#BD',
    'fmaj7': 'FACD#',
    'bmaj7': 'BD#F#A',
    'cmin7': 'CF#GB',
    'dmin7': 'DFAC',
    'gmin7': 'GC#DF',
    'fmin7': 'FG#CF#'
}

print('\n-------------------')
print('Welcome to Chordle!')
print('-------------------\n')

leveSelect = (input('SELECT YOUR LEVEL! Type !help for more information.\n(1) - EASY\n(2) - MEDIUM\n(3) - HARD\n'))

if (leveSelect == '!help'):
    print('')
    print('This is a game where you need to identify the chord or its notes with the hints that will be given!\n')
    print('You start with 0 points. Icrease your total points getting the questions right! \n')

    print('1 - Easy - Easy chords, major and minor default chords with 3 notes.')
    print('2 - Medium - Spicing up a little bit, the chords can now be major 7ths.')
    print('3 - Hard - All types of chords!')
    print('4 - Keep in mind that the half-step notes are all sharps! Do not use flats!\n')

    leveSelect = (input('SELECT YOUR LEVEL! Type !help for more information.\n(1) - EASY\n(2) - MEDIUM\n(3) - HARD\n'))


totalAttempts = 0
#LEVEL ONE CODE

if (leveSelect == '1'):
    print('')
    print('********************')
    print('LEVEL CHOSEN : EASY ')
    print('********************')
    print('')

    chordsInLevel = ['cmaj','dmaj','amaj','emaj','fmaj','bmaj']
    totalAttempts = 10
    correctAnswers =0
    
    for retries in range (1,totalAttempts +1):
    
        secretChord = random.choice(chordsInLevel)
        print(f'-----Attempt {retries} of {totalAttempts}-----')
        userInput = str (input(f'What are the notes of the following chord: {secretChord}'))
        userInput = userInput.replace(' ','')
        userInput = userInput.upper()

        if (len(userInput)<3 or len(userInput) > 20):
            print('That is not a valid answer!')
            continue

        elif (userInput == chordList[secretChord]):
            print('That is correct!')
            correctAnswers = correctAnswers + 1
            continue
        else:
            print('Thats incorrect!')
            continue

#LEVEL TWO CODE

if (leveSelect == '2'):
    print('')
    print('**********************')
    print('LEVEL CHOSEN : MEDIUM ')
    print('**********************')
    print('')
    chordsInLevel = ['cmaj','dmaj','amaj','emaj','fmaj','bmaj','cmaj7','dmaj','amaj7','emaj7','fmaj7','bmaj9','cmin7','dmin7','gmin7','fmin7']

    totalAttempts = 10
    correctAnswers = 0
    
    for retries in range (1, totalAttempts +1):

        secretChord = random.choice(chordsInLevel)
        chordsInLevel.remove(secretChord)

        print(f'-----Attempt {retries} of {totalAttempts}-----')
        userInput = str (input(f'What are the notes of the following chord: {secretChord}'))
        userInput = userInput.replace(' ','')
        userInput = userInput.upper()
        

        if (len(userInput)<3 or len(userInput) > 20):
            print('That is not a valid answer!')
            continue

        elif (userInput == chordList[secretChord]):
            print('That is correct!')
            correctAnswers = correctAnswers + 1
            continue
        else:
            print('Thats incorrect!')
            continue
# LEVEL 3 CODE 
# falta colocar os acordes adicionais dessa dificuldade.

if (leveSelect == '3'):
    print('')
    print('********************')
    print('LEVEL CHOSEN : HARD ')
    print('********************')
    print('')

    chordsInLevel =  ['cmaj','dmaj','amaj','emaj','fmaj','bmaj','cmaj7','dmaj','amaj7','emaj7','fmaj7','bmaj9','cmin7','dmin7','gmin7','fmin7']
    totalAttempts = 10
    correctAnswers = 0
    
    for retries in range (1, totalAttempts +1):
        
        
        secretChord = random.choice(chordsInLevel)
        chordsInLevel.remove(secretChord)

        print(f'-----Attempt {retries} of {totalAttempts}-----')
        userInput = str (input(f'What are the notes of the following chord: {secretChord}\n'))
        userInput = userInput.replace(' ','')
        userInput = userInput.upper()
    

        if (len(userInput)<3 or len(userInput) > 20):
            print('That is not a valid answer!\n')
            continue

        elif (userInput == chordList[secretChord]):
            print('That is correct!\n')
            correctAnswers = correctAnswers + 1
            continue

        else:
            print("That's incorrect!\n")
            continue     
            
if (totalAttempts == 10):
    points = correctAnswers * 100
    print(f'Your score was {points} points and you got a total of {correctAnswers} correct answer(s)    !\n')
    print('------------------------------')
    print('Thank you for playing Chordle!')
    print('------------------------------')
