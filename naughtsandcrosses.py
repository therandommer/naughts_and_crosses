# variables

# possible values include:
# - neutral
# X crosses
# O naughts
# gameGrid and gameGridText are for the basic game board
gameGrid = ["-" "-" "-" "\n" "-" "-" "-" "\n" "-" "-" "-" "\n"]
currentGameGrid = []  # will be updated during game loop
gameGridText = ",".join(currentGameGrid)
xScore = 0
oScore = 0
draws = 0
currentTurn = 1
currentTurnText = "O"

isGameOver = False  # run game logic while false, ask for rematch/reset when true

introText = "Welcome to naughts and crosses. \n"
currentTurnText = "It is", currentTurnText, "to go."
instructionText = "Please enter a number between 1-9"


# Initialise game state
def startGame():
    print(introText)
    currentGameGrid = gameGrid
    print(gameGridText)
    print(currentTurnText)
    print(instructionText)


# Handles the basic logic for getting input to correlate to each square
def getInput(input):
    if input.isnumeric():
        print("Input is numeric, do logic")
    elif input.isnumeric() and input == "0":
        print("Input is 0, return false")
    elif input.isnumeric() and input > 9:
        print("Input is too large, return false")
    else:
        print("Enter a valid number between 1-9, return false")


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
    currentInput = input()
    getInput(currentInput)

    if isGameOver:
        print("End of game", currentTurnText, "wins!")
        break  # exits game loop
    else:
        nextTurn()
