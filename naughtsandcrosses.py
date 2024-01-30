# variables

# possible values include:
# - neutral
# X crosses
# O naughts
# gameGrid and gameGridText are for the basic game board
gameGrid = ["-" "-" "-" "\n" "-" "-" "-" "\n" "-" "-" "-" "\n"]
gameGridText = ",".join(gameGrid)
xScore = 0
oScore = 0
draws = 0
currentTurn = 1
currentTurnText = "O"

isGameOver = False  # run game logic while false, ask for rematch/reset when true

introText = "Welcome to naughts and crosses. \nIt is", currentTurnText, "to go."


def startGame():
    print(introText)
    print(gameGridText)
