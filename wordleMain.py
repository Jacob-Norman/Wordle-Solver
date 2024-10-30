import wordleScraper as wScrape
import wordleSolver as wSolve
from wordleSolverFuncs import parseResult
from wordList import wordleList
from time import sleep

browser = wScrape.Browser()
browser.loginWordle()

wScrape.pageDown()

guessWord = "crane"
remainingWords = wordleList
guessedWords: list[str] = []

for attempt in range(6):
    wScrape.typeWord(guessWord)
    sleep(1.5)
    webResults: list[tuple] = wScrape.checkWord(browser, attempt + 1)
    if not('absent' in webResults) and not('present' in webResults):
        print("The word of the day is:", guessWord)
        break
    results = parseResult(guessWord, webResults)
    (guessWord, remainingWords, guessedWords) = wSolve.bestGuess(results, remainingWords, guessedWords)
    sleep(1)

# allows the user to view the solved puzzle, Program will end when browser is closed anyway
sleep(300)
