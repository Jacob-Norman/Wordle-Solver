from wordleSolverFuncs import possibleCheckList
import wordleSolver_bruteForce as bruteForce
import wordleSolver_letterAlgo as letterAlgo


def bestGuess(result: list[tuple], possibleWords: list[str], guessedWords: list[str]):
    remainingWords: list[str] = possibleCheckList(result, possibleWords)

    if len(remainingWords) == 0:
        print("Error! This word is not in the word bank.")
        return('zzzzz', remainingWords, guessedWords) 
    elif len(remainingWords) <= 2:
        if not(remainingWords[0] in guessedWords):
            guess = remainingWords[0]  
        else:
            guess = remainingWords[1]

        guessedWords.append(guess)
        return(guess, remainingWords, guessedWords)
    elif len(remainingWords) <= 50:
        guess = bruteForce.bestGuess(remainingWords, guessedWords)
        guessedWords.append(guess)
        return(guess, remainingWords, guessedWords)
    else:
        guess = letterAlgo.bestGuess(remainingWords, guessedWords)
        guessedWords.append(guess)
        return(guess, remainingWords, guessedWords)