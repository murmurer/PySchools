#Topic 7 Question 21
#Write a function isAllLettersUsed(word, required) that takes in a word as the
#first argument and returns True if the word contains all the letters found in
#the second argument.

def isAllLettersUsed(word, required):

    for ch in word:
        if ch in required:
            return True
        else:
            return False
            end