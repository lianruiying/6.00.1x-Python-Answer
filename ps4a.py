# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open('C:/Users/lianr/Desktop/6001x/words.txt', 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    if len(word)==0:
        return 0
    for char in word:
        score += SCRABBLE_LETTER_VALUES[char]
    score = score*len(word)
    if len(word) == n:
        score += 50
    return score



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
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
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    

    copy = hand.copy()
    for item in copy:
        for char in word:
            if char == item:
                copy[item] -= 1
    return copy



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    
    copy = hand.copy()
    if word in wordList:
        for char in word:
            try:
                copy[char] -= 1
                value = copy[char] 
                if value == -1:
                    return False
            except KeyError:
                return False
        return True
    else:
        return False


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):

    count = 0
    for i in hand:
        count += hand[i]
    return count
    


def playHand(hand, wordList, n):
    score = 0
    while True:  
        u = 0   
        for i in hand:
            u += hand[i]    
        if u != 0:
            print 'Current Hand:',
            displayHand(hand)
            word = raw_input('Enter word, or a \".\" to indicate that you are finished: ')  
            if word == '.':
                print 'Goodbye! Total score: ',score,'points'
                break          
            elif not isValidWord(word, hand, wordList):
                print 'Invalid word, please try again.'
                print ' '
                continue
            else: 
                hand = updateHand(hand, word)
                score += getWordScore(word, n)
                print '\"'+word+'\"','earned',getWordScore(word, n),'points.','Total:',score,'points'
                print ' '       
                        
        else:
#            print '\"'+word+'\"','earned',getWordScore(word, n),'points.','Total:',score,'points'
#            print ''
            print 'Run out of letters. Total score:',score,'points'
            break
            
            
# Problem #5: Playing a game
# 

def playGame(wordList):
    while True:
        bura = 0
        game = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if game == 'n':
            #n = raw_input('How many letter do you want: ')
            bura += 1
            hand = dealHand(7)
            playHand(hand, wordList, 7)
        elif game == 'r':
            if bura != 0:
                playHand(hand, wordList, 7) 
            else:
                print 'You have not played a hand yet. Please play a new hand first!'
        elif game == 'e':
            break 
            
        else:
            print 'Invalid command.'
#    print "playGame not yet implemented." # <-- Remove this line when you code the function
   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
