import numpy as np
import random

class AI1():
    # Define settings upon initialization. Here you can specify
    def __init__(self, numRows, numCols, numBombs, safeSquare):   

        # game variables that can be accessed in any method in the class. For example, to access the number of rows, use "self.numRows" 
        self.numRows = numRows
        self.numCols = numCols
        self.numBombs = numBombs
        self.safeSquare = safeSquare
        self.listOfBombs = []
        self.safeSquareSet = set()

    def open_square_format(self, squareToOpen):
        return ("open_square", squareToOpen)

    def submit_final_answer_format(self, listOfBombs):
        return ("final_answer", listOfBombs)

    # (helper function): return true if and only if a square (r, c) is within the game grid
    def squareInBounds(self, r, c):
        return r >= 0 and c >= 0 and r < self.numRows and c < self.numCols

    # helper function that adds neighbors of zero squares as safe squares
    def add_zero_neighbors(self, boardState, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.squareInBounds(row + i, col + j) and boardState[row + i][col + j] == -1):
                    self.safeSquareSet.add(((row + i, col + j), -1));

    # helper function that finds squares that we can absolutely say are bombs given number information
    def find_confirmed_bombs(self, boardState, row, col):
        uncoveredOrBombs = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.squareInBounds(row + i, col + j) and (boardState[row + i][col + j] == -1 or self.listOfBombs.__contains__((row + i, col + j)) or boardState[row + i][col + j] == 9)):
                    uncoveredOrBombs.append((row + i, col + j))
        
        if (len(uncoveredOrBombs) == boardState[row][col]):
            for uncoveredOrBomb in uncoveredOrBombs:
                if (not(self.listOfBombs.__contains__(uncoveredOrBomb))):
                    self.listOfBombs.append(uncoveredOrBomb)

    # helper function that finds squares that are definitely safe             
    def find_safe_squares(self, boardState, row, col):
        safeNeighbors = []
        bombNeighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.squareInBounds(row + i, col + j) and (self.listOfBombs.__contains__((row + i, col + j)) or boardState[row + i][col + j] == 9)):
                    bombNeighbors.append((row + i, col + j))
                elif (self.squareInBounds(row + i, col + j)):
                    safeNeighbors.append((row + i, col + j))
        if (len(bombNeighbors) == boardState[row][col]):
            for safeNeighbor in safeNeighbors:
                if (boardState[safeNeighbor[0]][safeNeighbor[1]] == -1):
                    self.safeSquareSet.add((safeNeighbor, -1))
    
    def analyze_square(self, boardState, row, col):
        if (boardState[row][col] == 0):
            self.add_zero_neighbors(boardState, row, col)
        else:
            if (not(self.listOfBombs.__contains__((row, col)))):
                if (boardState[row][col] == 9):
                    self.listOfBombs.append((row, col))
                else:
                    self.find_confirmed_bombs(boardState, row, col)
            self.find_safe_squares(boardState, row, col)


    # return the square (r, c) you want to open based on the given boardState
    # the boardState will contain the value (0-8 inclusive) of the square, or -1 if that square is unopened
    # an AI example that returns a random square (r, c) that you want to open
    def performAI(self, boardState):
        print(boardState)

        # find all the unopened squares
        unopenedSquares = []
        for row in range(self.numRows):
            for col in range(self.numCols):
                if (boardState[row][col] == -1 and not(self.listOfBombs.__contains__((row, col)))):
                    unopenedSquares.append((row, col))

        if (len(self.listOfBombs) == self.numBombs):
            # If the number of unopened squares is equal to the number of bombs, all squares must be bombs, and we can submit our answer
            # print(f"List of bombs is {self.listOfBombs}")
            return self.submit_final_answer_format(self.listOfBombs)
        else:
            # Otherwise, pick a random square and open it
            for row in range(self.numRows):
              for col in range(self.numCols):
                self.analyze_square(boardState, row, col)

            # Make sure that our random choice isn't a confirmed bomb
            for bomb in self.listOfBombs:
                if (unopenedSquares.__contains__(bomb)):
                    unopenedSquares.remove(bomb)
            # Open confirmed safe squares
            if(not(len(self.safeSquareSet) == 0)):
                squareToOpen = random.sample(self.safeSquareSet, 1)[0][0]
            else:
                if (len(unopenedSquares) == 0):
                    # print(f"List of bombs is {self.listOfBombs}")
                    return self.submit_final_answer_format(self.listOfBombs)
                squareToOpen = random.choice(unopenedSquares)
            self.safeSquareSet = set()
            # print(f"Square to open is {squareToOpen}")
            return self.open_square_format(squareToOpen)
        
