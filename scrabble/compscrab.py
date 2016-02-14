from userscrab import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives the maximum value score, and return it.

    """
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score=0

    # Create a new variable to store the best word seen so far (initially None)
    best=None  

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            temp_score=getWordScore(word, n)
            if temp_score>max_score:
                max_score=temp_score
                best=word

    # return the best word you found.
    return best


#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):

    totscore=0
    while calculateHandlen(hand)>0:
        
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        
               
        ans =compChooseWord(hand, wordList, n)
        if ans==None:
            break
            
        ans=str(ans)
        current_score=getWordScore(ans, n)
        totscore+=current_score
        hand=updateHand(hand, ans)
        ans='"'+ ans + '"'
        print ans +" earned "+ str(current_score) +" points."+"Total: "+str(totscore)+" points\n"
        

                

    print "Total score: " +str(totscore)+" points" 
#
# Playing a game
#
#
def playGame(wordList):

    counter=0
    
    while True:
        
        reply=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        
        
        if reply=='e':
            break
            
        elif reply!='n' and reply!='r':
            print "Invalid command."
            
        else:
             
            if reply=='n':
                checker=0
                while checker==0: 
                    choice=raw_input( "Enter u to have yourself play, c to have the computer play: ") 
                    
                    if choice=='c':
                        hand=dealHand(HAND_SIZE)   
                        compPlayHand(hand, wordList,HAND_SIZE)
                        counter=1
                        checker+=1
                    elif choice=='u':
                        hand=dealHand(HAND_SIZE)
                        playHand(hand, wordList,HAND_SIZE)
                        counter=1
                        checker+=1
                    else:
                        print "Invalid command."
                        
            elif reply=='r':
                checker=0   
                if counter==1:
                    while checker==0: 
                        choice=raw_input( "Enter u to have yourself play, c to have the computer play: ") 
                        if choice=='c':   
                            compPlayHand(hand, wordList,HAND_SIZE)       
                            checker+=1
                        elif choice=='u':
                            playHand(hand, wordList,HAND_SIZE)  
                            checker+=1
                        else:
                            print "Invalid command."
                    
                else:
                    print "You have not played a hand yet. Please play a new hand first!"
      
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    


