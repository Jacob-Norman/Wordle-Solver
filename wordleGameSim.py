from wordleSolverFuncs import repCheck

def game(answer: str, guess: str):
    result: list[str] = []
    for i in range(5):
        if guess[i] == answer[i]:
            result.append("correct")
        elif guess[i] in answer:
            answerReps = repCheck(guess[i], answer)
            if repCheck(guess[i], guess) <= answerReps:
                result.append("present")
            else:
                # check for how many of the repetitions are correct.
                correct = 0
                for j in range(5):
                    if guess[j] == guess[i] and guess[j] == answer[j]:
                        correct += 1
                if answerReps == correct:
                    result.append("absent")
                else:
                    repsGuessed = correct
                    for k in range(5):
                        if repsGuessed == answerReps:
                            result.append("absent")
                            break
                        elif k == i:
                            result.append("present")
                            break
                        elif guess[k] == guess[i] and result[k] == "present":
                            repsGuessed += 1
        else:
            result.append("absent")
    return(result)