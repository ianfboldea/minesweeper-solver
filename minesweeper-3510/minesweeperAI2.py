import random
import numpy as np
import math
import rref

class AI2():

    # Define settings upon initialization. Here you can specify
    def __init__(self, numRows, numCols, numBombs, safeSquare):   

        # game variables that can be accessed in any method in the class. For example, to access the number of rows, use "self.numRows" 
        self.numRows = numRows
        self.numCols = numCols
        self.numBombs = numBombs
        self.safeSquare = safeSquare
        self.listOfBombs = []
        self.constraintGridIndex = 0
        self.constraintGrid = []
        for i in range(0, numRows*numCols):
            self.constraintGrid.append([])
        for row in self.constraintGrid:
            for i in range(0, numRows*numCols):
                row.append(0)
        self.constraintSums = []
        for i in range(0, numRows*numCols):
            self.constraintSums.append(0)
        self.knownSquares = []
        for i in range(0, numRows):
            self.knownSquares.append([])
        for row in range(0, numRows):
            for col in range(0, numCols):
                self.knownSquares[row].append(-1)
        self.knownSquares[safeSquare[0]][safeSquare[1]] = 10

    def open_square_format(self, squareToOpen):
        return ("open_square", squareToOpen)

    def submit_final_answer_format(self, listOfBombs):
        return ("final_answer", listOfBombs)

    # (helper function): return true if and only if a square (r, c) is within the game grid
    def squareInBounds(self, r, c):
        return r >= 0 and c >= 0 and r < self.numRows and c < self.numCols
    
    def check_for_bombs(self, augmentedMatrix):
        for i in range (0, len(augmentedMatrix)):
            if augmentedMatrix[i][len(augmentedMatrix[i])-1] == 0:
                for j in range (0, len(augmentedMatrix[i])):
                    if augmentedMatrix[i][j] != 0:
                        # print((math.floor(j/10),j%10))
                        self.knownSquares[math.floor(j/10)][j%10] = 10
            else:
                tiles = []
                for j in range (0, len(augmentedMatrix[i])-1):
                    if augmentedMatrix[i][j] == 1:
                        tiles.append((i, j))
                if augmentedMatrix[i][len(augmentedMatrix[i])-1] == len(tiles):
                    for tile in tiles:
                        if not(self.listOfBombs.__contains__((math.floor(tile[1]/10), tile[1]%10))):
                            self.listOfBombs.append((math.floor(tile[1]/10), tile[1]%10)) 

    def solve_constraints(self):
        temp = self.constraintGrid[:][:]
        for i in range (0, len(self.constraintSums)):
            temp[i].append(self.constraintSums[i])
        self.check_for_bombs(temp)
        if not(self.numCols*self.numRows > 300):
            augmentedMatrix = rref.rref(np.array(temp, dtype='float'))
            self.check_for_bombs(augmentedMatrix)                 
    
    def add_constraint(self, boardState, row, col):
        constraintSum = boardState[row][col]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if ((i == 0 and j == 0) or not(self.squareInBounds(row+i, col+j))):
                    continue
                elif (self.knownSquares[row+i][col+j] == -1):
                    # If we don't know the value
                    self.constraintGrid[self.constraintGridIndex][(row+i)*10 + (col+j)] = 1
                else:
                    # If we already know the value
                    if self.knownSquares[row+i][col+j] == 9 or self.listOfBombs.__contains__((row+i, col+j)):
                        constraintSum -= 1
        self.constraintSums[self.constraintGridIndex] = constraintSum
        self.constraintGridIndex += 1

    # return the square (r, c) you want to open based on the given boardState
    # the boardState will contain the value (0-8 inclusive) of the square, or -1 if that square is unopened
    # an AI example that returns a random square (r, c) that you want to open
    # TODO: implement a better algorithm
    def performAI(self, boardState):
        # find all the unopened squares
        safeSquares = []
        unopenedSquares = []
        for row in range(self.numRows):
            for col in range(self.numCols):
                if boardState[row][col] == -1:
                    unopenedSquares.append((row, col))
                else:
                    self.knownSquares[row][col] = boardState[row][col]
                    if boardState[row][col] == 9:
                        if not(self.listOfBombs.__contains__((row, col))):
                            self.listOfBombs.append((row, col))
                    else:
                        self.add_constraint(boardState, row, col)
        self.solve_constraints()
        for row in range(self.numRows):
            for col in range(self.numCols):
                if (self.knownSquares[row][col] == 10):
                    safeSquares.append((row, col))
        for i in range(0, len(self.constraintGrid)):
            for j in range(0, len(self.constraintGrid[i])):
                self.constraintGrid[i][j] = 0
        for i in range(0, len(self.constraintSums)):
            self.constraintSums[i] = 0
        self.constraintGridIndex = 0
        if len(self.listOfBombs) == self.numBombs:
            return self.submit_final_answer_format(self.listOfBombs)
        else:
            # Otherwise, pick a random square and open it
            squareToOpen = None
            if (len(safeSquares) > 0):
                squareToOpen = random.choice(safeSquares)
            else:
                squareToOpen = random.choice(unopenedSquares)
            print("Square to open is {}".format(squareToOpen))
            return self.open_square_format(squareToOpen)