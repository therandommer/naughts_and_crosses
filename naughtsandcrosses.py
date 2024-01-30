# variables

# possible values include:
# - neutral
# X crosses
# O naughts
# gameGrid and gameGridText are for the basic game board
gameGrid = "-" "-" "-" "-" "-" "-" "-" "-" "-"
currentGameGrid = gameGrid  # will be updated during game loop
xScore = 0
oScore = 0
draws = 0
currentTurn = 1
currentTurnText = "O"

# game logic loopers
hasInput = False  # used to loop input getter unti valid input received
isGameOver = False  # run game logic while false, ask for rematch/reset when true

introText = "Welcome to naughts and crosses. \n"
currentTurnText = "It is", currentTurnText, "to go."
instructionText = "Please enter a number between 1-9"


# Initialise game state
def startGame():
    print(introText)
    print(printGameGrid())
    print(currentTurnText)


def printGameGrid():
    gameGridText = "".join(str(currentGameGrid))
    return "\n".join(gameGridText[i : i + 3] for i in range(0, len(gameGridText), 3))


# Handles the basic logic for getting input to correlate to each square
def getInput(input):
    if input.isnumeric() and int(input) > 0 and int(input) < 10:
        print("Input is numeric, do logic")
        # add input to check if a square is occupied or not
        return True
    else:
        print("Input is not valid, return false")
        return False


# will be called after every valid input, just before the end of game logic if the game is not over
def nextTurn():
    if currentTurn == 1:
        currentTurn == 2
        currentTurnText == "X"
    elif currentTurn == 2:
        currentTurn == 1
        currentTurnText == "O"


# game loop starts here
startGame()

while not isGameOver:
    print(instructionText)
    currentInput = input()

    if not hasInput:
        hasInput = getInput(currentInput)
    else:
        print("Continue game logic")
        if isGameOver:
            print("End of game", currentTurnText, "wins!")
            break  # exits game loop
        else:
            nextTurn()
