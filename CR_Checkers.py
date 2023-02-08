"""
- Using a 2D list
- create a representation of a checkers board's starting state (just the player positions)
- N.B. You do not have to make any game functionality
- Just a 2D list containing the starting state.
- pass in the square board's size as a parameter
- the minimum board size is 8, each player should have three rows of checkers
- checkers should alternate
- one player has red checkers (R)
- one player has white checkers (W)

Additionally please make a function to print out the checkerboard neatly (you may use whatever suitable symbols you like)

The board of size 8 should look like this (just a representation) (_ represents an empty space, R represents a red checker, W represents a white Checker, spaces are not required)

_ R _ R _ R _ R
R _ R _ R _ R _
_ R _ R _ R _ R
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ W _ W _ W _ W
W _ W _ W _ W _
_ W _ W _ W _ W
"""
import sys

def printBoard(board):
    for row in board:
        for column in row:
            print(column + " ",end="")
        print()


def genBoard(size):
    # generate a matrix of the size mentioned, 
    # but every other square, if the square is in the top three rows, add an "R"
    # and for every other square, if the square is in the bottom three rows, add a "W"

    if size < 8:
        sys.exit("ERROR - minimum size is 8")

    flip = "odd"
    # create base board
    board = []
    for row in range(size):
        # create a new row
        board.append([])
        for column in range(size):
            if flip == "even":
                if row <= 2 and column % 2 == 0:
                    board[row].append("R")
                elif row > size-4 and column % 2 == 0:
                    board[row].append("W")
                else:
                    board[row].append("_")
            else:
                if row <= 2 and column % 2:
                    board[row].append("R")
                elif row > size-4 and column % 2:
                    board[row].append("W")
                else:
                    board[row].append("_")
        if flip == "odd":
            flip = "even"
        else:
            flip = "odd"
    return board

printBoard(genBoard(8))