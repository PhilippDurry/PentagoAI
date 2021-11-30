import Main

empty = '◦'
white = '●'
black = '○'


def calculateAITurn(board, aiColor):
    possiblePlays = []

    # white lines are counted positive, black lines negative
    # the most impactful AI play is the play with the highest absolute line count
    # it either is a play to improve the AI's own position or to deny the opponent's best plays
    # location, tileNumber, rotationDirection, lineCount
    mostImpactfulPlay = [(0, 0), 0, "", 0]

    # iterating over the whole board and looking for empty spots
    for row in range(6):
        for col in range(6):
            if board[row][col] == empty:
                # set a marble on empty spot
                board[row][col] = aiColor

                # try out all 8 possible tile rotations and for each get the highest number of equal marbles in a line
                for tileNumber in range(4):

                    board = Main.rotateTileClockwise(tileNumber, board)
                    highestLineCount = getHighestNumberOfMarblesInALine(board)

                    if abs(highestLineCount) > abs(mostImpactfulPlay[3]):
                        mostImpactfulPlay[0] = (row, col)
                        mostImpactfulPlay[1] = tileNumber
                        mostImpactfulPlay[2] = "clockwise"
                        mostImpactfulPlay[3] = highestLineCount

                    # revert tile rotation
                    board = Main.rotateTileAntiClockwise(tileNumber, board)

                    # rotate into other direction
                    board = Main.rotateTileAntiClockwise(tileNumber, board)
                    highestLineCount = getHighestNumberOfMarblesInALine(board)

                    if abs(highestLineCount) > abs(mostImpactfulPlay[3]):
                        mostImpactfulPlay[0] = (row, col)
                        mostImpactfulPlay[1] = tileNumber
                        mostImpactfulPlay[2] = "anticlockwise"
                        mostImpactfulPlay[3] = highestLineCount

                    # revert tile rotation
                    board = Main.rotateTileClockwise(tileNumber, board)

                # remove the marble and look for next empty spot
                board[row][col] = empty

    location = mostImpactfulPlay[0]
    tileNumber = mostImpactfulPlay[1]
    rotationDirection = mostImpactfulPlay[2]
    rotation = [tileNumber, rotationDirection]
    return location, rotation


# count white marbles positive and black negative
def getHighestNumberOfMarblesInALine(board):
    highestLineCount = 0

    # count in all 6 rows
    for row in range(6):
        tmpCount = 0
        lastMarble = empty
        for col in range(6):
            thisMarble = board[row][col]
            # if current marble is different from last, then reset counter and update highest line count
            tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
            lastMarble = thisMarble
        if abs(tmpCount) > abs(highestLineCount):
            highestLineCount = tmpCount

    # count in all 6 columns
    for col in range(6):
        tmpCount = 0
        lastMarble = empty
        for row in range(6):
            thisMarble = board[row][col]
            # if current marble is different from last, then reset counter and update highest line count
            tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
            lastMarble = thisMarble
        if abs(tmpCount) > abs(highestLineCount):
            highestLineCount = tmpCount

    # count in 6 middle diagonals
    # 1 short diagonal
    tmpCount = 0
    lastMarble = empty
    for i in range(5):
        thisMarble = board[i][i + 1]
        # if current marble is different from last, then reset counter and update highest line count
        tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
        lastMarble = thisMarble
    if abs(tmpCount) > abs(highestLineCount):
        highestLineCount = tmpCount

    # 2 long diagonal
    tmpCount = 0
    lastMarble = empty
    for i in range(6):
        thisMarble = board[i][i]
        # if current marble is different from last, then reset counter and update highest line count
        tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
        lastMarble = thisMarble
    if abs(tmpCount) > abs(highestLineCount):
        highestLineCount = tmpCount

    # 3 short diagonal
    tmpCount = 0
    lastMarble = empty
    for i in range(5):
        thisMarble = board[i + 1][i]
        # if current marble is different from last, then reset counter and update highest line count
        tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
        lastMarble = thisMarble
    if abs(tmpCount) > abs(highestLineCount):
        highestLineCount = tmpCount

    # 4 short diagonal
    tmpCount = 0
    lastMarble = empty
    for i in range(5):
        thisMarble = board[i][4 - i]
        # if current marble is different from last, then reset counter and update highest line count
        tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
        lastMarble = thisMarble
    if abs(tmpCount) > abs(highestLineCount):
        highestLineCount = tmpCount

    # 5 long diagonal
    tmpCount = 0
    lastMarble = empty
    for i in range(6):
        thisMarble = board[i][5 - i]
        # if current marble is different from last, then reset counter and update highest line count
        tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
        lastMarble = thisMarble
    if abs(tmpCount) > abs(highestLineCount):
        highestLineCount = tmpCount

    # 6 short diagonal
    tmpCount = 0
    lastMarble = empty
    for i in range(5):
        thisMarble = board[i + 1][5 - i]
        # if current marble is different from last, then reset counter and update highest line count
        tmpCount, highestLineCount = compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount)
        lastMarble = thisMarble
    if abs(tmpCount) > abs(highestLineCount):
        highestLineCount = tmpCount

    return highestLineCount


def compareMarbles(thisMarble, lastMarble, tmpCount, highestLineCount):
    if thisMarble != lastMarble:
        if abs(tmpCount) > abs(highestLineCount):
            highestLineCount = tmpCount
        tmpCount = 0
    if thisMarble == white:
        tmpCount += 1
    if thisMarble == black:
        tmpCount -= 1
    return tmpCount, highestLineCount


'''
# ----------------------------------------------------------------------
def main():
    Main.printBoardState()
    highestLineCount = getHighestNumberOfMarblesInALine(board)
    print(highestLineCount)


if __name__ == "__main__":
    # execute only if run as a script
    main()
'''
