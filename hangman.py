import random
import getpass
import re

ERROR = 101
CORRECT = 102
WRONG = 103

def main():
    again = True
    while again == True:
        word = setUp()
        game( word )
        again = playAgain()
    print("END PROGRAM")
    print("==============================================================\n")



def game( word ):
    availableLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    wordBlanks = []
    for index in word:
        wordBlanks.append("_")
    print("HANGMAN GAME\n============")
    lives = 6
    correctGuesses = 0
    while lives > 0 and correctGuesses != len(word):
        displayLives( lives, word )
        displayGuessedWord( wordBlanks )
        displayLetters( availableLetters )
        result, guess = getAndCheckInput( availableLetters, word )
        if result == WRONG:
            lives -= 1
        elif result == CORRECT:
            correctGuesses  = updateGuessedWord( wordBlanks, word,
                                                        guess, correctGuesses )
        updateLetters( availableLetters, guess, word )

    if lives == 0:
        displayLives( lives, word )
    else:
        displayWin( lives, word )


def updateGuessedWord( wordBlanks, word, guess, correctGuesses ):
    if len(guess) == len(word):
        correctGuesses = len(guess)
    else:
        for index in range(len(word)):
            if guess == word[index]:
                wordBlanks[index] = guess
                correctGuesses += 1
    return correctGuesses

def updateLetters( availableLetters, guess, word ):
    if len(guess) != len(word):
        for index in range(len(availableLetters)):
            if guess == availableLetters[index]:
                availableLetters[index] = "_"

def getAndCheckInput( availableLetters, word ):
    userGuess = input("Guess: ").upper()
    print("")
    if len(userGuess) == 0:
        print("Enter a letter or word")
        returnResult =  ERROR
    elif len(userGuess) == 1:
        if not checkLetterInSet( userGuess, availableLetters ):
            print("You already tried that letter")
            returnResult =  ERROR
        elif checkLetterInSet( userGuess, word ):
            print("Correct Letter")
            returnResult =  CORRECT
        else:
            print("Wrong Letter")
            returnResult =  WRONG
    else:
        returnResult = WRONG
        if len(userGuess) == len(word):
            sameLetters = True
            for index in range(len(word)):
                if word[index] != userGuess[index]:
                    sameLetters = False
            if sameLetters:
                print("Correct Word")
                returnResult = CORRECT
            else:
                print("Wrong Word")

        else:
            print("Wrong Word")
    return returnResult, userGuess

def checkLetterInSet(testChar, dataSet):
    for index in dataSet:
        if testChar == index:
            return True
    return False

def setUp():
    print("\n==============================================================")
    print("HANGMAN GAME SETUP:\n===================")
    correctPlayerCount = False
    while correctPlayerCount == False:
        players = input( "One <1> Or Two <2> Players: " )
        if players == "2":
            correctWord = False
            while not correctWord:
                word = getpass.getpass(prompt="Word to be guessed: ")
                if bool(re.search(r"\s", word)):
                    print("Don't include any spaces")
                elif len(word) == 0:
                    print("Input word to be guessed")
                elif not word.isalpha():
                    print("Letters only")
                else:
                    correctWord = True
            correctPlayerCount = True
        elif players == "1":
            print("retriving random word from word bank ...",end="")
            word = wordBank()
            print(" random word retrieved")
            correctPlayerCount = True
        else:
            print("ERROR: Enter <1> or <2>")
    print("==============================================================")
    return word.upper()

def wordBank():
    with open("words.txt","r") as words:
        wordList = []
        for word in words:
            wordList.append(word.strip("\n"))
        randWord = random.randint(0,len(wordList) - 1)
    return wordList[randWord]

def playAgain():
    print("==============================================================")
    again = input("Press <y> to play again: " )
    print("==============================================================")
    if again.upper() == 'Y':
        return True
    return False

def displayLetters( letters ):
    print("Letters:",end=" ")
    for index in letters:
        print(index,end=" ")
    print("")

def displayGuessedWord(wordBlanks):
    print("Word:",end=" ")
    for index in wordBlanks:
        print(index, end=" ")
    print("")

def displayLives( lives, word ):
    match lives:
        case 0:
            print(
f"""    ______
    |    |
    |               Guesses Left: {lives}
    |   ___
    |  |RIP|        The Word Was: {word}
    |  |   |
""")

        case 1:
            print(
f"""    ______
    |    |
    |    O          Guesses Left: {lives}
    |
    |
    |
""")

        case 2:
            print(
f"""    ______
    |    |
    |    O          Guesses Left: {lives}
    |    |
    |
    |
""")

        case 3:
            print(
f"""    ______
    |    |
    |    O          Guesses Left: {lives}
    |    |\\
    |
    |
""")

        case 4:
            print(
f"""    ______
    |    |
    |    O          Guesses Left: {lives}
    |   /|\\
    |
    |
""")

        case 5:
            print(
f"""    ______
    |    |
    |    O          Guesses Left: {lives}
    |   /|\\
    |   /
    |
""")

        case 6:
            print(
f"""    ______
    |    |
    |    O          Guesses Left: {lives}
    |   /|\\
    |   / \\
    |
""")

def displayWin( lives, word ):
            print(
f"""    ______
    |    |
    |               Guesses Left: {lives}
    |   \\O/
    |    |      Hooray! The Word Was: {word}
    |   / \\
""")


main()
