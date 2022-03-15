import os
cols = 10
bombs = 10
safeX = 0
safeY = 3
algoNumber = 2
numTrials = 5
for r in range (10, 101, 10):
  if ((r % 2) == 0):
    os.system("python minesweeperPerformanceTest.py -g {} {} {} {} {} {} {}".format(r, cols, r, safeX, safeY, algoNumber, numTrials))
  else:
    os.system("python minesweeperPerformanceTest.py -g {} {} {} {} {} {} {}".format(cols, r, r, safeX, safeY, algoNumber, numTrials))