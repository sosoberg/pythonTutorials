secretWord = "giraffe"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False

# as long as the guess does not equal the secret word, continue to ask the prompt

while guess != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        guess = input("Please input the secret word: ")
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print("Sorry, you are out of guesses!")
else:
    print("Correct!")
