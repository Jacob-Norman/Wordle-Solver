from validList import validWords
from wordleGameSim import game
from wordleSolver import possibleCheckList
from wordleSolverFuncs import parseResult
from wordleSolver_letterAlgo import letterScore

import time as t

# priorityList returns all letter in the alphabet in left to right order of which letters
# occur in closest to half the words. It is very unlikely that any word that does not contain
# at least on of the top three letters is going to be the best guess. This function eliminates
# bad guesses from the wordle list so that we can increase the cap for where we use the brute force method
def filterGuessWords(words: list[str]):
    priorityList = letterScore(words)
    filteredList: list[str] = []
    for word in validWords:
        if priorityList[0] in word or priorityList[1] in word:
            filteredList.append(word)

    return filteredList

def bestGuess(remainingWords: list[str], guessedWords: list[str]):
    filteredList = filterGuessWords(remainingWords)
    remainingAmount = [0] * len(filteredList)

    for answer in remainingWords:
        index = 0
        for guess in filteredList:
            # Ensures that none of the guessed words are guessed again as wordle will not allow it
            if guess in guessedWords:
                remainingAmount[index] = 10000000
            else:
                simResult = game(answer, guess)
                result = parseResult(guess, simResult)
                remainingWordsLen = len(possibleCheckList(result, remainingWords))
                remainingAmount[index] += remainingWordsLen 
                index += 1
    
    min_val = min(remainingAmount)
    minGuesses: list[str] = []
    for i in range(len(filteredList)):
        if remainingAmount[i] == min_val:
            minGuesses.append(filteredList[i])
    
    guess = "xxxxx"
    guessSet = False
    for word in remainingWords:
        if word in minGuesses:
            guess = word
            guessSet = True
            break
    
    if not(guessSet):
        guess = minGuesses[0]
    
    return(guess)