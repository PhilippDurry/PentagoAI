import AI

# ----------   GLOBAL VARIABLES   ---------- #
empty = '◦'
white = '●'
black = '○'

board = [[empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty]]


# --------------   MAIN CODE   -------------- #

def main():
    printBoardState()

    playerColor, aiColor = choosePlayerColor()
    if playerColor == white:
        readTurnFromConsole(playerColor)
    while True:
        aiMakesATurn(aiColor)
        readTurnFromConsole(playerColor)


# --------------   FUNCTIONS   -------------- #

def aiMakesATurn(color):
    location, rotation = AI.calculateAITurn(board, color)

    print("\nAI spielt: " + str(location))
    placeMarbleOnBoard(location, color)
    printBoardState()

    print("\nAI dreht: " + "Quadrat " + str(rotation[0]) + " " + rotation[1])
    if rotation[1] == "clockwise":
        rotateTileClockwise(rotation[0], board)
    if rotation[1] == "anticlockwise":
        rotateTileAntiClockwise(rotation[0], board)
    printBoardState()


def choosePlayerColor():
    string = input("\nChoose your color:\n1: white\n2: black\n")
    if string == '1':
        return white, black
    if string == '2':
        return black, white


def readTurnFromConsole(color):
    string = input("\nDu bist am Zug...\nWo möchtest Du spielen?  z.B.: 0,5\n")
    location = (int(string[0]), int(string[2]))
    placeMarbleOnBoard(location, color)
    printBoardState()

    string = input("\nWelches Quadrat willst Du drehen? 0,1,2 oder 3?  Im/gegen den Uhrzeigersinn?  z.B.: 2g oder 0i\n")
    tileNumber = int(string[0])
    if string[1] == 'i':
        rotateTileClockwise(tileNumber, board)
    else:
        rotateTileAntiClockwise(tileNumber, board)
    printBoardState()


def printBoardState():
    print(" ________________________________")

    for row in range(6):
        print("|                              \u2009\u2009\u2009\u2009\u2009\u2009\u2009\u2009|")

        print('|', end='')
        for col in range(6):
            print(' ', board[row][col], ' ', end='')
        print('|')

    print(" ________________________________")


# give location in cartesian (X,Y) coordinates   <<<------------- geändert!!!!!
def placeMarbleOnBoard(location, color):
    # col = location[0] - 1
    # row = 6 - location[1]
    board[location[0]][location[1]] = color


def rotateTileClockwise(tileNumber, board):
    # calculate offsets depending on tile to be turned
    y_off = 0
    x_off = 0
    if tileNumber == 1:
        x_off += 3
    if tileNumber == 2:
        y_off += 3
    if tileNumber == 3:
        y_off += 3
        x_off += 3

    # shift corners
    tmp = board[0 + y_off][0 + x_off]
    board[0 + y_off][0 + x_off] = board[2 + y_off][0 + x_off]
    board[2 + y_off][0 + x_off] = board[2 + y_off][2 + x_off]
    board[2 + y_off][2 + x_off] = board[0 + y_off][2 + x_off]
    board[0 + y_off][2 + x_off] = tmp
    # shift middles
    tmp = board[0 + y_off][1 + x_off]
    board[0 + y_off][1 + x_off] = board[1 + y_off][0 + x_off]
    board[1 + y_off][0 + x_off] = board[2 + y_off][1 + x_off]
    board[2 + y_off][1 + x_off] = board[1 + y_off][2 + x_off]
    board[1 + y_off][2 + x_off] = tmp

    return board


def rotateTileAntiClockwise(tileNumber, board):
    board = rotateTileClockwise(tileNumber, board)
    board = rotateTileClockwise(tileNumber, board)
    board = rotateTileClockwise(tileNumber, board)
    return board


if __name__ == "__main__":
    # execute only if run as a script
    main()


