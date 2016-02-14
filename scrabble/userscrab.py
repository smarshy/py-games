

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "F:/vatsala/scrabble/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    """
    score=0
    length=len(word)
    for i in word:
        score+=SCRABBLE_LETTER_VALUES[i] 
        
    score=score*length
        
    if length==n:
        score+=50
    
    return score
    

def displayHand(hand):
    """
    Displays the letters currently in the hand.
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Updating a hand by removing letters
#
def updateHand(hand, word):

    temphand=hand.copy()
    
    for letter in word:
        temphand[letter]-=1
            
    return temphand


#
# Testing word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely composed of letters in the hand.
    """
    existence=True
    temphand=hand.copy()
    
    if word not in wordList:
        existence=False
    
    for letter in word:
        if letter not in temphand:
            existence=False
        else:
            temphand[letter]-=1
    
    for letter in temphand:
        if temphand[letter]<0:
            existence=False
            
    return existence


#
# Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    """
    return sum(hand.itervalues())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand
      
    """
    
    # Keep track of the total score
    totscore=0
    message="Run out of letters. "
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand)>0:
        
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        
               
        ans = raw_input('Enter word, or a "." to indicate that you are finished:')
        ans=str(ans)
        
        # If the input is a single period:
        if ans=='.':
            message="Goodbye! "
            break
        
        else:
            
            if isValidWord(ans, hand, wordList)==False:
                print"Invalid word, please try again."
            
            else:
                current_score=getWordScore(ans, n)
                totscore+=current_score
                print ans +" earned "+ str(current_score) +" points."+"Total: "+str(totscore)+" points\n"
                hand=updateHand(hand, ans)

                

    print message + "Total score: " +str(totscore)+" points"


#
# Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands. 
    """
    counter=0
    while True:
        
        reply=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if reply=='e':
            break
        elif reply=='n': 
            hand=dealHand(HAND_SIZE)
            playHand(hand, wordList,HAND_SIZE)
            counter=1
        elif reply=='r':
            if counter==1:
                playHand(hand, wordList,HAND_SIZE)
            else:
                print "You have not played a hand yet. Please play a new hand first!"
            
        else:
            print "Invalid command."
            

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
