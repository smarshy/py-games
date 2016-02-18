
import string
import random

WORDLIST_FILENAME = "F:/vatsala/python/words.txt"

# -----------------------------------
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("F:/vatsala/python/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    shift: 0 <= int < 26
    """
    dict1={}
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    main=upper+lower    
    for i in range(0,len(main)):
        if i<len(upper):
            letter=upper[i]
            if i+shift<len(upper):
                dict1[letter]=upper[i+shift]
            else:
                dict1[letter]=upper[shift-(len(upper)-i)]
        else:
            letter=lower[i-26]
            if i-26+shift<len(lower):
                dict1[letter]=lower[i-26+shift]
            else:
                
                dict1[letter]=lower[shift-(len(main)-i)]
    return dict1 

    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.
    """
    encoded=""
    for letter in text:
        if letter.isalpha():
            encoded=encoded+coder[letter]
        else:
            encoded=encoded+letter
    return encoded

def applyShift(text, shift):
    """
    returns: text after being shifted by specified amount.
    """
    
    shifted=buildCoder(shift)
    return applyCoder(text, shifted)

#
# Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    """
    real=0
    best_shift=0
    for shift in range(0,26):
        valid=0
        shifted=applyShift(text, shift)
        found=shifted.split(' ')
        for word in found:
            if isWord(wordList, word):
                valid+=1
        if valid>real:
            best_shift=shift
            real=valid
    return best_shift    
            


def decryptStory():

    encrypted=getStoryString()
    bestShift = findBestShift(wordList, encrypted)
    return applyShift(encrypted, bestShift)
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    
    """s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    print applyShift(s, bestShift)
    assert applyShift(s, bestShift) == 'Hello, world!'"""
    print decryptStory()
