from random import randint

hangman = [
    '''
        --------
        |      |
        |      
        |    
        |      
        |     
        -
    ''',
    '''
        --------
        |      |
        |      O
        |    
        |      
        |     
        -
    ''',
    '''
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        -
    ''',
    '''
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        -
    ''',
    '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     
        -
    ''',
    '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        -
    ''',
    '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
    '''
]

words = ['colors', 'painting', 'canvas', 'pallete']
word = words[randint(0,len(words)-1)]

current_word = ['_' for _ in word]
errors = []
inpt = ""

print('Welcome to a "Hangman" game!')

while '_' in current_word:
    print(hangman[len(errors)])
    print("Word: ", *current_word, sep='')
    print("Errors:", ', '.join(errors))
    print("Error count:", len(errors))
    
    inpt = input("Enter a character in this word: ")[0]
   
    if inpt not in word:
        errors.append(inpt)
    else:
        i = 0
        
        for _ in range(word.count(inpt)):
            i = word.find(inpt, i)
            current_word[i] = inpt
            i += 1

    if len(errors) == 6:
        print("\n" + hangman[len(errors)])
        print("You have lost!")
        break
else:
    print('\nYes, the right word is "', word, '"!')
    print("Congratulations! You won!")