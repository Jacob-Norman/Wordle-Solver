import wordleScraper as wScrape
import wordleSolver as wSolve
from wordleSolverFuncs import parseResult
from wordList import wordleList
from time import sleep
import sys  # Import sys to exit the program

browser = wScrape.Browser()
browser.loginWordle()

wScrape.pageDown()

guessWord = "crane"
remainingWords = wordleList
guessedWords: list[str] = []

for attempt in range(6):
    # Check if the browser is closed
    if browser.isBrowserClosed():
        print("The browser was closed. Exiting program.")
        sys.exit()  # Exit the program if the browser is closed
    
    wScrape.typeWord(guessWord)
    sleep(1.5)
    webResults: list[tuple] = wScrape.checkWord(browser, attempt + 1)
    if not('absent' in webResults) and not('present' in webResults):
        print("The word of the day is:", guessWord)
        break
    results = parseResult(guessWord, webResults)
    (guessWord, remainingWords, guessedWords) = wSolve.bestGuess(results, remainingWords, guessedWords)
    sleep(1)

while True:
    if browser.isBrowserClosed():
        print("The browser was closed. Exiting program.")
        sys.exit()  # Exit the program if the browser is closed
