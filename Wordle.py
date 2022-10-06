# Copyright Tiffani Shilts Portland, OR April 2022

# name: Wordle.py

# description: program that imitates the popular wordle game
# the user tries to guess a five letter word by entering guesses
# of five letter words. After every guess, the user is provided hints
# if the letter is an exact match a * is printed in its place
# if the letter is contained in the word (and was not also guessed 
# correctly) a + will be printed. If the same letter is entered multiple
# times, + will only appear for the same amount of times that the letter
# is contained in the secret word (like wordle)
# if the letter is not contained in the word, it has already been 
# guessed, or the number of times the letter appears is greater than that
# contained in the secret word, a . will be printed in its place

from random import randint

import string


def wordle(numTries = 5):
    
    print("\n")
    
    # initialize word list
    
    words = ["apple", "about", "carrot", "zebra", "table", "scarf", 
             "dozen"]
    
    # pick a secret word and ensure it is indeed five letters
    
    secretWord = ""
    
    while len(secretWord) != 5:
    
        secretWord = words[randint(0,6)]
    
    # prompt the user for the specified number of tries. 
    # five is the default
    
    for i in range(numTries):
        
        # initialize variables
            
        guessOutput = [0, 0, 0, 0, 0]
        
        userInput = ""
        
        # prompt user for word
        # ensure it is five letters and does not contain digits
        
        active = True
        
        while active:
        
            userInput = input("Guess: ")
            
            # remove all whitespace
            
            userInput = userInput.translate(str.maketrans(" ", " ", " "))
            
            # remove punctuation characters
            
            userInput = userInput.translate(str.maketrans("", "", string.punctuation))
            
            # remove digits
            
            userInput = userInput.translate(str.maketrans("", "", string.digits))
            
            if len(userInput) != 5:
            
                print("need a five letter guess")
                continue
            
            else:
                
                active = False
        
        # convert to lower to correct for user input differences
        
        userInput = userInput.lower()
        
        # if the user has guessed the word inform them and end the 
        # program
        
        if userInput == secretWord:
                
            print("Huzzah!")
            print("thanks for playing (:")
            print("\n")
            break
        
        # loop through the user input and first find exact matches
        # after exact matches, check for letters contained in secret
        # word but input in wrong position. remove letters in temp 
        # secret word as they are "used" so that the program doesn't say
        # an identical letter is contained in a word in which the match 
        # has already been found and that when the same character is 
        # input in the wrong position only the amount of occurrences 
        # contained in the secret word are shown as + (as wordle does)
        
        tempSecretWord = secretWord
             
        for j in range(5):
            
            if userInput[j] == secretWord[j]:
                
                guessOutput[j] = "*"
                
                tempSecretWord = tempSecretWord[:j] + "0" + tempSecretWord[(j+1):]
                
        for k in range(5):
                
            if userInput[k] in tempSecretWord:
                
                guessOutput[k] = "+"
                
                tempSecretWord = tempSecretWord.replace(userInput[k], "0", 1)
                
            elif userInput[k] != secretWord[k]:
                
                guessOutput[k] = "."
                
        # output result to user
        
        print("%d: %s %s%s%s%s%s" % ((i + 1), userInput, guessOutput[0], 
                                  guessOutput[1], guessOutput[2], 
                                  guessOutput[3], guessOutput[4]))
    
    # once the for loop completes i.e the number of tries have been depleted
    # alert user they are out of tries
            
    else:
            
        print("sorry, too many guesses")
        print("\n")
            
            
            
            
            
            
            
            
                
        