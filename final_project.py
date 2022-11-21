import random
import re
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
       ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
    +---+
    O   |
   /|   |
       |
       ===''', '''
    +---+
     O   |
    /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
     ===''']

with open("words.txt", "r") as f:
    words = f.read()
words = words.split("\n")

def randomword(wordlist):
    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]

def board(wrongletters, correctletters, actualword):
    print(HANGMAN_PICS[len(wrongletters) - 1])
    print()

    print('wrong letters:', end =' ')
    #end=' ' replaces newline character that is printed after the string with a single space character
    for letter in wrongletters:
        print(letter, end=' ')
    print()
    space = '_' * len(actualword)
    for i in range(len(actualword)):
        if actualword[i] in correctletters:
            space = space[:i] + actualword[i] + space[i+1:]

    for letter in space:
        print(letter, end=' ')
    print()

def guessword(guess_made):
    while True:
        print("Guess a letter:")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Invalid. Please enter one letter only.")
        elif guess in guess_made:
            print("You've already guessed this letter. Please make another guess.")
        else:
            return guess

def regame():
    print("Do you want to play again?")
    answer = str(input())
    yes_regex = re.compile(r"(y|Y|yes|Yes)")
    no_regex = re.compile(r"(n|N|no|No)")
    if re.match(yes_regex, answer):
        return True 
    else:
        return False

print("H A N G M A N")
wrongletters = " "
correctletters = " "
actualword = randomword(words)
end_game = False
won = False

while True:
    board(wrongletters, correctletters, actualword)
    guess = guessword( wrongletters + correctletters )
    if guess in actualword:
        correctletters += guess
        guessed_all = True
        for i in range(len(actualword)):
            if actualword[i] not in correctletters:
                guessed_all = False
        if guessed_all:
            print("Congratulations. You won. The letter required is " + actualword)
            end_game = True
            won = True
    else:
        wrongletters += guess

        if len(wrongletters) == len(HANGMAN_PICS) - 1:
            board(wrongletters, correctletters, actualword)
            print("You have lost. The word needed was " + actualword + ".")
            end_game = True 
    if end_game:
        if not won:
            print(HANGMAN_PICS[len(wrongletters)])
        if regame():
            wrongletters = " "
            correctletters = " "
            end_game = False
            actualword = randomword(words)
            won = False
        else:
            break 


