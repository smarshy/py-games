
# Hangman game


import random
import string

WORDLIST_FILENAME = "F:/vatsala/hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=0
    for letter in secretWord:
        if letter not in lettersGuessed:
           return False
        else:
           count+=1
    
    if len(secretWord)==count: 
        return True
        

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed=""
    for letter in secretWord:
        if letter in lettersGuessed:
           guessed+=" " +letter
        else:
           guessed+=" " +"_"
    
    return guessed



def getAvailableLetters(lettersGuessed):

    import string
    avail=string.ascii_lowercase
    
    for letter in lettersGuessed:
        if letter in avail:
            avail=avail.replace(letter,"")
    return avail
    

def hangman(secretWord):
    '''

    Starts up an interactive game of Hangman.

    * After each round, displays to the user the partially guessed word so far, as well as letters that the user has not yet guessed.

    '''
    letters=[]
    guessno=8
    length=len(secretWord)
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+ str(length) + " letters long."
    print "-----------"
            
            
    while guessno>0:
        print "You have " + str(guessno)+" guesses left."
        previous_guess=getGuessedWord(secretWord, letters)
        print "Available Letters: " + getAvailableLetters(letters)
        guess =raw_input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        
        if guessInLowerCase not in letters:
            letters.append(guessInLowerCase)
            current_guess=getGuessedWord(secretWord, letters)
            if current_guess!=previous_guess:
                message="Good guess: "
            else:
                message="Oops! That letter is not in my word: "
                guessno-=1
                
        else:
            current_guess=previous_guess
            message="Oops! You've already guessed that letter: "
            
        print message + current_guess
        
        print "-----------"
        
        if isWordGuessed(secretWord, letters):
            print "Congratulations, you won!"
            break
            
    if isWordGuessed(secretWord, letters)==False:
        print "Sorry, you ran out of guesses. The word was "+secretWord+"."
    

secretWord = chooseWord(wordlist).lower()

#secretWord = "apple"
hangman(secretWord)
