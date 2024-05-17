from wordList import wordleList
from wordleGameSim import game
from wordleSolver import possibleCheckList
from wordleSolverFuncs import parseResult

import time as t

def bestGuess(remainingWords: list[str], guessedWords: list[str]):
    remainingAmount = [0] * 2309
    for answer in remainingWords:
        index = 0
        for guess in wordleList:
            # Ensures that none of the guessed words are guessed again as wordle will not allow it
            if guess in guessedWords:
                remainingAmount[index] = 1000000
                index += 1
                continue
            simResult = game(answer, guess)
            result = parseResult(guess, simResult)
            remainingAmount[index] += len(possibleCheckList(result, remainingWords))
            index += 1
    
    min_val = min(remainingAmount)
    minGuesses: list[str] = []
    for i in range(2309):
        if remainingAmount[i] == min_val:
            minGuesses.append(wordleList[i])
    
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