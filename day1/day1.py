# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    calories = []
    calories.append([])
    for line in inputFile.readlines():
        if line == '\n':
            calories.append([])
        else:
            calories[-1].append(int(line))


    # Close the file and return the result
    inputFile.close()
    return calories

# Puzzle 1
def puzzle1(filename):
    # Read file
    inputs = input_parser(filename)
    return max([sum(cal) for cal in inputs])

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)
    caloriesSorted = [sum(cal) for cal in inputs]
    caloriesSorted.sort()
    return sum(caloriesSorted[-3:])

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 24000
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 45000
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))