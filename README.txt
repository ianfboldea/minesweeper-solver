Ian Boldea, iboldea3@gatech.edu, April 30, 2021

Files Submitted in the Root Directory:
plots:
These contain all of the plots that were made in order to produce the project report pdf

README.txt:
This file

project_report.pdf:
The project report pdf

Files Submitted in /minesweeper-3510:
Starter Code:
Files including Generate.py, minesweeperGameEngine.py, minesweeperPerformance.py, and test_board.json were all provided by the 
CS3510 TAs and they remain unchanged from what they were originally given to me as. To see how to use these files (which is not
necessary to run my project), see the starter code folder.

data.py, data2.py:
These files get data automatically written to them by the writeData.py files. They contain a series of append statements
appending to the trials array once data is written to them. See writeData.py, writeData2.py to see how data is written to
them. The important thing to note is that these files are nearly identical. If you wish to store data in data2.py instead
of data.py or vice versa, you must go into minesweeperPerformanceTest.py, Ctrl+f, and change "data.py" to "data2.py" or 
vice versa.

writeData.py, writeData2.py:
These files write data to the data.py and data2.py files respectively. They contain a series of intuitively named
variables that prompt you to enter the size of the board you want to generate, what your starting safe square will be,
which algorithm you wish to use, the number of bombs per grid, and how many trials you wish to conduct for each 
increment of variable. Using for loops, you are able to vary one or more of the variables to conduct testing on the 
algorithms. In each writeData.py file, an example for loop is already completed. You may use this for loop, which was
used to produce the plots for the project, or you may vary the for loop. These files essentially runs the
minesweeperPerformance.py file with a randomly generate board given all the constraints.

plot.py, plot2.py, plot3.py, plot4.py:
These files make use of matplotlib to plot data from data.py and data2.py in a pretty way. Essentially, if you run 
each one of them, you will get all 4 graphs you need for the project. You need to change the title in each tile to
Algorithm A or Algorithm B based on the algorithm you are analyzing, and otherwise, the files remains the same.

rref.py:
This file is a custom file whose inspiration was definitely gathered online. This performs gaussian elimination on a
numpy matrix recursively. This is the bread and butter helper function of algorithm 2.

minesweeperAI1.py:
This file contains algorithm 1. The general structure parallels the one given to me in the starter code files. The entire
description of how the algorithm functions exactly is given in the project report pdf, but essentially, I have several
global variables and several helper functions that help me to identify easy patterns and clues about which tiles are safe
and which tiles are bombs. 

minesweeperAI2.py:
This file contains algorithm 2. Again, I utilized the same structure as the one given to me in the starter code files,
and the detailed description of how this file functions is given in the project report pdf, but I essentially try to 
perform a simplified version of the constraint satisfaction problem. I have several global variables and helper functions
that enable me to save constraints across each iteration through the board and simplify these constraints using 
gaussian elimination in order to identify known safe squares and known bomb squares.

In Order to Run The Program:
In order to run the program for the purposes of compiling charts to visualize algorithmic accuracy, simply fill in the 
variables in writeData.py or writeData2.py based on the values you would like the randomly generated grids to have. 
If you wish to vary one of the variables, you may do so with a for loop in writeData.py or writeData2.py, as shown in the
respective files. If you are using writeData.py, don't forget to go into minesweeperPerformanceTest.py, Ctrl+f, and search
for "data.py" or "data2.py" and update the string with the same number of writeData.py you are using (i.e. data2.py for 
writeData2.py). 

Once writeData.py or writeData2.py is filled in with the appropriate algorithm, grid, and number of trials 
specifications, run the appropriate file by doing:
> python writeData.py
OR
> python writeData2.py

In order to see the data that was just written from writeData.py or writeData2.py, simply run the appropriate plot.py file:
> python plot.py
> python plot2.py
> python plot3.py
> python plot4.py

In order to visualize how the algorithm works, you can run the minesweeperGamePerfomance.py file like so:
> python minesweeperGameEngine.py -f test_board.json
and navigate through the GUI. You may change "test_board.json" to any file in any of the board folders provided in the
starter code on canvas.

Known Bugs/Limitations:
As detailed in the project report pdf, algorithm 2 cannot row reduce past a board size of about 300 tiles. This is due
to the large recursion stack that is caused by having a constraint matrix of the size of the board to the power of 2.
The algorithm still works on large sized boards, however, it is just highly inefficient.