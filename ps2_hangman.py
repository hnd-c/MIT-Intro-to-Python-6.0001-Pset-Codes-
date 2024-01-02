# Problem Set 2, hangman.py
# Name: Hem N Chaudhary
# Collaborators:None
# Time spent:Few Days

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lsw=0  #legth of secretworld 
    for letter in secret_word:
        if letter in letters_guessed: #compares the guesses with the words in the secretword
             lsw+=1
                        
               
    
    if lsw==len(secret_word): #checks if all the words were guessed 
        vtr=True            #vtr=value to be returned
    else:
        vtr=False
    
    return vtr           


def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result=''                
    for lett1 in secret_word:
        if lett1 in letters_guessed: #if guessed word is in secret word, gets added in result
            result+=lett1
        else:                #if gussed word not in secret word, add *
            result+='*'
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    a=string.ascii_lowercase
    b=list(a)                       #converting alphabet string to a list
    for letter1 in letters_guessed:
        if letter1 in b:
            b.remove(letter1)      #removing all the letters that has been guessed so far
    result=''.join(b)#converting a list to string
                  
    return result
    

def letter_to_reveal(secret_word,available_letter):
    '''
    secret_word: string, the lowercase word the user is guessing
    available_letter:string, comprised of letters that represents which
      letters have not yet been guessed
    
    '''
    choose_from=''
    for i in available_letter:
        if i in secret_word:
            choose_from+=i          #collecting all the words in secret word that has not been guessed yet
    
    new = random.randint(0, len(choose_from)-1) #randomly selecting a word that has not been guessed
    revealed_letter = choose_from[new]
    return revealed_letter



def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '^'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol ^, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("--------------")
    
    #finding uniq number of letters in secret word
    uniq_lett=''.join(set(secret_word))
    
    nguess=10 #number of guesses left
    winloss_ind=False #win/loss indicator
    progress=''
    lgword1=[]          #list for guessed word
    while nguess>0:        #iterating over the number of guess left
        print("You have",nguess,"guesses left.") 
        aletter=get_available_letters(lgword1) #listing all the availabe choices
        print("Available letters:",aletter,end='')
        gword=input("Please guess a letter:") #getting input
        lgword=gword.lower()                 #converting the alphabets to lower case
        lgword1+=lgword                     #adding guessed letters to the list
        progress=get_word_progress(secret_word,lgword1)
        if len(lgword)==1 and (lgword.isalpha()): #checking if the input is one word and valid
            if lgword in secret_word and lgword in aletter:              
                if progress==secret_word:             #checking if the secret word has been guessed
                    print("Good Progress:",progress)
                    print("--------------")
                    print("Congratulations, you won!")
                    score=(2*nguess*int(len(uniq_lett)))+(3*int(len(secret_word))) #score formula
                    print("Your total score for this game is:",score)
                    winloss_ind=True
                    break                     #breaks the loop if the secret word has been guessed
                else:
                    print("Good Progress:",progress)
                    print("--------------")
            elif (lgword not in secret_word) and (lgword in 'aeiou'): #checks and penalizes if the guessed vowel is not in the secret word
                print("Oops! That letter is not in my word:",progress)
                print("--------------")
                nguess-=2
                
            else:
                print("Oops! That letter is not in my word:",progress)
                print("--------------")
                nguess-=1
                
        elif with_help and len(lgword)==1 and gword=='^': #reveal a word in the secret word that hasn't been guessed if the condition is met
            if nguess<3:
                print("Oops! Not enough guesses left:",progress)
                print("--------------")
            else:
                rev_letter=letter_to_reveal(secret_word,aletter)
                lgword1+=rev_letter    #adding the revealed word in guessed list
                progress=get_word_progress(secret_word,lgword1)
                nguess-=3
                print("Letter revealed:",rev_letter) #reveaks a random word in secret word 
                if progress==secret_word:
                    print("Good Progress:",progress)
                    print("--------------")
                    print("Congratulations, you won!")
                    score=(2*nguess*int(len(uniq_lett)))+(3*int(len(secret_word))) #score formula
                    print("Your total score for this game is:",score)
                    winloss_ind=True
                    break                 #breaks the loop when secret word is guessed
                else:
    
                    print(progress)
                    print("--------------")
                    #print(nguess)
        
        else:                           #checks When the input is not valid
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:",progress)
            print("--------------")
    
            
    if winloss_ind==False: #gets invoked when win requirement is not met and number of guess is zero
        print("Sorry, you ran out of guesses. The word was",secret_word +'.')

        
        
        
        
    
        
        
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
       # secret_word = choose_word(wordlist)
       # with_help = True
       # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "^" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

# Test hangman function
   # word='wildcard'
   # hangman(word,True)