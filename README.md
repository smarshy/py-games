# py-games
Comprises of Hangman & Scrabble games, a Sudoku checker script and a cipher decryption app. 
Some of these have been developed while undertaking MOOCS.

Rules for hangman:

    * At the start of the game, the user will be told how many letters 
      the secretWord contains and the number of guesses you have.

    * The user can supply one guess (i.e. letter) per round.

    * Immediate feedback will be given after each guess 
      about whether the guess appears in the computers word.

    * After each round,the partially guessed word would be displayed, 
      along with the letters that haven't been guessed yet.
     
    * If the word is not guessed within the given number of chances,
      the user loses and then the secret word would be disclosed


Rules for Scrabble:

For a particular hand -

    * The hand is displayed.
    
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
      
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
      
    * When a valid word is entered, it uses up letters from the hand.
    
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
      
    * The sum of the word scores is displayed when the hand finishes.
    
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
      
Allows the user to play an arbitrary number of hands-
Asks the user to input 'n' or 'r' or 'e'-

    * Input 'n' to play a new (random) hand.
    
    * Input 'r' to play the last hand again.
    
    * Input 'e', to exit the game.
      
To play against the computer type 'c' when prompted else 'u'to have yourself play.  

For cipher decryption, you can input the encrypted text (by substituting shifted letters) in a text file and let the computer try to decode it for you

To run any game, simply run the respective script - hangman.py / compscrab.py or userscrab.py / encrypt_decrypt.py