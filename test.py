from wordleSolver import bestGuess
from wordleSolverFuncs import parseResult
from wordleGameSim import game
from wordList import wordleList
import time as t

def test(startWord):
    tooManyTries: list[str] = []
    attemptNum = 0

    tryCounter = [0] * 6
    timePerTryCount = [0] * 6

    for answer in wordleList:
        start = t.time()
        guessWord = startWord
        remainingWords = wordleList
        guessedWords: list[str] = []
        tries = 0

        for attempt in range(6):
            simResults = game(answer, guessWord)
            if not('absent' in simResults) and not('present' in simResults):
                tries += 1
                break
            results = parseResult(guessWord, simResults)
            (guessWord, remainingWords, guessedWords) = bestGuess(results, remainingWords, guessedWords)
            tries += 1
            t.sleep(1)
        attemptNum += 1

        end = t.time()

        tryCounter[tries - 1] += 1
        timePerTryCount[tries - 1] += (end - start)

        if tries > 6:
            tooManyTries.append(answer)
            
    totalTime = 0
    totalTries = 0

    averageTime = [0] * 6
    for i in range(6):
        totalTime += timePerTryCount[i]
        totalTries += tryCounter[i] * (i + 1)
        if tryCounter[i] != 0:
            averageTime[i] = timePerTryCount[i]/tryCounter[i]


        
    print("\n\nWords that took to many tries are", tooManyTries, "\n")

    for i in range(6):
        print("For solves that took", i + 1, "attempts:")
        print("There was a total of:", tryCounter[i])
        print("The average time for solves of this size is:", averageTime[i])
        print("\n")

    print("The general average solve time is:", totalTime/2309)
    print("The average number of attempts is:", totalTries/2309, "\n")
    print("This sim took a total of:", totalTime/60, "minutes.")