def repCheck(letter: str, word: str):
    reps = 0
    for l in word:
        if l == letter:
            reps += 1
    return reps

def possibleCheckList(result: list[tuple], optionalWords: list[str]):
    remainingWords: list[str] = []
    correctLetters: str = ""
    for pair in result:
        if pair[1] == "correct":
            correctLetters += pair[0]

    for word in optionalWords:
        lettersInAnswer: str = correctLetters
        possible = True
        index = 0
        for pair in result:
            if pair[1] == 'correct':
                correctCheck = pair[0] == word[index]
                if not correctCheck:
                    possible = False
                    break

            elif pair[1] == 'present':
                if pair[0] in lettersInAnswer:
                    lettersInAnswer += pair[0]
                    repetitionsLTorEQ = repCheck(pair[0], lettersInAnswer) <= repCheck(pair[0], word)
                    if not repetitionsLTorEQ or pair[0] == word[index]:
                        possible = False
                        break
                else:
                    presentCheck = pair[0] in word and pair[0] != word[index]
                    if not presentCheck:
                        possible = False
                        break
                    else:
                        lettersInAnswer += pair[0]

            elif pair[1] == 'absent':
                if pair[0] in lettersInAnswer:
                    repetitionsMatch = repCheck(pair[0], lettersInAnswer) == repCheck(pair[0], word)
                    if not repetitionsMatch:
                        possible = False
                        break
                else:
                    absentCheck = not(pair[0] in word)
                    if not absentCheck:
                        possible = False
                        break
            else:
                print("Error 'a' has occurred")
            index += 1

        if possible:
            remainingWords.append(word)
    return remainingWords

def parseResult(word: str, result: list[str]):
    parsedResult: list[tuple] = []
    for i in range(5):
        parsedResult.append((word[i], result[i]))
    return parsedResult
