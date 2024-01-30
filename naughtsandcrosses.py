# variables

# possible values include:
# numbers = neutral
# X crosses
# O naughts
# gameGrid and gameGridText are for the basic game board
gameGrid = "1" "2" "3" "4" "5" "6" "7" "8" "9"
currentGameGrid = gameGrid  # will be updated during game loop
xScore = 0
oScore = 0
draws = 0
currentTurn = 1
gameLength = 1
currentTurnVal = "O"
# game logic loopers
hasInput = False  # used to loop input getter unti valid input received
isGameOver = False  # run game logic while false, ask for rematch/reset when true

introText = "Welcome to naughts and crosses. \n"
instructionText = "Please enter a number between 1-9"


# Initialise game state
def startGame():
    print(introText)
    print("Turn: " + str(gameLength))
    printGameGrid()
    print("It is " + currentTurnVal + " to go.")


def printGameGrid():
    gameGridText = "".join(str(currentGameGrid))
    return print(  # adds line separators for user view
        "\n".join(gameGridText[i : i + 3] for i in range(0, len(gameGridText), 3))
    )


# Handles the basic logic for getting input to correlate to each square
def getInput(input):
    if input.isnumeric() and int(input) > 0 and int(input) < 10:
        if currentGameGrid.find(str(input)) == -1:
            print("Choose a different square")
            return False
        return True
    else:
        return False


def updateGrid(indexNo):
    global currentGameGrid
    newGameGrid = str(currentGameGrid)
    newGameGrid = newGameGrid.replace(str(indexNo), str(currentTurnVal))
    currentGameGrid = newGameGrid


# will be called after every valid input, just before the end of game logic if the game is not over
def nextTurn():
    global currentTurn
    global currentTurnVal
    global gameLength
    if currentTurn == 1:
        currentTurn = 2
        currentTurnVal = "X"
    elif currentTurn == 2:
        currentTurn = 1
        currentTurnVal = "O"
    global hasInput
    hasInput = False
    gameLength += 1
    print("Turn: " + str(gameLength))
    printGameGrid()
    print("It is " + str(currentTurnVal) + " to go.")


def checkForWinner():
    global currentGameGrid
    thisGameGrid = str(currentGameGrid)


# game loop starts here
startGame()

while not isGameOver:
    if not hasInput:
        print(instructionText)
        currentInput = input()
        hasInput = getInput(currentInput)
    else:
        updateGrid(currentInput)
        if isGameOver:
            print("End of game" + currentTurnVal + "wins!")
            break  # exits game loop
        else:
            nextTurn()
