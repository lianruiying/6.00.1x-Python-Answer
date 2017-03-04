# -*- coding: utf-8 -*-
import random
import string


def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open('C:\Users\lianr\Desktop\words.txt', 'r', 0)
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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    bark = True
    count = 0
    while count <= len(secretWord):
        for i in secretWord:
            if i in lettersGuessed:
                continue
            else:
                bark = False
        count += 1   
    return bark


def getGuessedWord(secretWord, lettersGuessed):
    feedback = []
    ind = 0
    ans = ''
    for cou in range(len(secretWord)):    
        feedback.append('_ ')
    for char in secretWord:
        if char in lettersGuessed:
            if char not in feedback:
                ind = secretWord.index(char)
                feedback[ind] = char 
            else:
                position = -1
                for s in secretWord:
                    position +=1
                    if s == char:               
                        feedback[position] = char  
        else:
            continue
    for i in feedback:
        ans += i  
    return ans


def getAvailableLetters(lettersGuessed):
    alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in lettersGuessed:
        if char in alf:
            alf.remove(char)
    output = ''
    for al in alf:
        output += al
    return output   
     
secretWord = chooseWord(wordlist)

def hangman(secretWord):
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    countTime = 8
    lettersGuessed = []
    while countTime >0:
        print 'You have '+str(countTime)+' guesses left.'
        print 'Available letters: '+getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()  #要不要删？        
        countTime -= 1
        if guess in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter: '+getGuessedWord(secretWord, lettersGuessed)
            continue
        elif guess not in lettersGuessed:
            lettersGuessed.append(guess)         
            if guess in secretWord:
                print 'Good guess: '+getGuessedWord(secretWord, lettersGuessed)
            else:          
                print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed)                 
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            break
    if not isWordGuessed(secretWord, lettersGuessed):
        print 'Sorry, you ran out of guesses. The word was else.'

# secretWord = chooseWord(wordlist).lower()
hangman('tact')
