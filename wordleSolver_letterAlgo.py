from validList import validWords

def letterScore(words: list[str]):
    occurrences = [0] * 26
    for word in words:
        lettersInWord: list[str] = []
        for letter in word:
            # ensures letter is only counted once per word.
            if not(letter in lettersInWord):
                occurrences[ord(letter) - 97] += 1
                lettersInWord.append(letter)

    halfOccurrenceScore: list[float] = []
    for i in occurrences:
        halfOccurrenceScore.append(abs((i / len(words)) - 0.5))
    # numbers closer to 0 in halfOccurrenceScore are letters that occur in closer to half the words

    priorityList: list[str] = []
    excisingIndex : list[int] = []

    for repetition in range(26):
        min = 1.0
        minIndex = 0
        for i in range(26):
            if halfOccurrenceScore[i] < min and not(i in excisingIndex):
                min = halfOccurrenceScore[i]
                minIndex = i
        excisingIndex.append(minIndex)
        priorityList.append(chr(minIndex + 97))

    return priorityList

def wordsContaining(letters: list[str]):
    for word in validWords:
        possible = True
        for letter in letters:
            if not(letter in word):
                possible = False
                break
        if possible:
            return word
    return "none"

def wordsContainingByPriorityList(priorityList: list[str], index: list[int]):
    letters: list[str] = []
    for i in range(len(index)):
        letters.append(priorityList[index[i]])
    return wordsContaining(letters)

def bestWord(sequence: list[int], priorityList: list[str], guessedWords):
    guess = wordsContainingByPriorityList(priorityList, sequence)
    if guess != 'none' and not(guess in guessedWords):
        return guess
    cap = 25
    length = len(sequence)
    endIndex = length - 1
    if length == 1 and sequence[0] == cap:
        # this base case is for safety and will never be reached reaching this point implies that
        # no words exist with a any of the single letters of index positions up to the cap
        return "zebra"
    elif sequence[endIndex] != cap:
        sequence[endIndex] += 1
        return bestWord(sequence, priorityList, guessedWords)
    elif sequence[endIndex] == cap and sequence[endIndex - 1] != cap - 1:
        sequence[endIndex - 1] += 1
        sequence[endIndex] = sequence[endIndex - 1] + 1
        return bestWord(sequence, priorityList, guessedWords)
    else:
        tempSequence: list[int] = []
        for i in range(length - 1):
            tempSequence.append(i)
        sequence = tempSequence
        return bestWord(sequence, priorityList, guessedWords)

def bestGuess(remainingWords: list[str], guessedWords: list[str]):
    priorityList = letterScore(remainingWords)
    startSequence = [0, 1, 2, 3, 4]
    guess = bestWord(startSequence, priorityList, guessedWords)
    return(guess)