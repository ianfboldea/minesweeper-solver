import os
cols = 20
rows = 50
safeX = 0
safeY = 3
algoNumber = 2
numTrials = 5
for bombs in range (20, 201, 20):
  os.system("python minesweeperPerformanceTest.py -g {} {} {} {} {} {} {}".format(rows, cols, bombs, safeX, safeY, algoNumber, numTrials))