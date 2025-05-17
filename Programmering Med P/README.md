### Python Program - Laboration 3 

## Overview
This program reads the CSV file, classifies them based based on the line of best fit and saves the classified data into a new CSV file. Displays plot with scatter and line to visually show the two grouped classificated points and where they are splitet.

## How the program works
Input: It reads the default unlabelled_data.csv file, you have ability to change the variable file value to import your own file. but the file needs to contain two columns which represents x, y coordinates. Uses functions to find and apply for classifications of each point as Class above and Class below which represents points above or below the line. This applies on first degree linear equations (y = kx + m).

Output: Saves the classified points into labelled_data.csv. It will produce three colums representing x-axis, y-axis and class. Make sure to change the value (path) of the write file variable if you dont want to overwrite it, after each run of the program. The program also displays a plot with blue dots representing class above line and class below line which are splitet by the green line which represents line of best fit.

## Languages 
Python 3

## Modules
# Default-
itertools

# Third party, pip
numpy
matplotlib.pyplot

# Caution
Make sure to use Rainbow CSV extension to be able to switch into ; as a derimeter to view this type of csv file through VS code as itended. 

# Credits
Sebastian Plucinski
