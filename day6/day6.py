# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    line = inputFile.read()

    # Close the file and return the result
    inputFile.close()
    return line

# Puzzle 1
def puzzle1(filename):
    # Read file
    inputs = input_parser(filename)

    result = 4
    while len(set(inputs[result-4:result])) != 4:
        result += 1

    return result

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)

    result = 14
    while len(set(inputs[result-14:result])) != 14:
        result += 1

    return result

# Run tests for puzzle 1
puzzle1Result1 = puzzle1('example1')
puzzle1Result2 = puzzle1('example2')
puzzle1Result3 = puzzle1('example3')
puzzle1Result4 = puzzle1('example4')
puzzle1Result5 = puzzle1('example5')
puzzle1TestPass = puzzle1Result1 == 7 and puzzle1Result2 == 5 and puzzle1Result3 == 6 and puzzle1Result4 == 10 and puzzle1Result5 == 11
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result1}, {puzzle1Result2}, {puzzle1Result3}, {puzzle1Result4}, {puzzle1Result5}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2Result1 = puzzle2('example1')
puzzle2Result2 = puzzle2('example2')
puzzle2Result3 = puzzle2('example3')
puzzle2Result4 = puzzle2('example4')
puzzle2Result5 = puzzle2('example5')
puzzle2TestPass = puzzle2Result1 == 19 and puzzle2Result2 == 23 and puzzle2Result3 == 23 and puzzle2Result4 == 29 and puzzle2Result5 == 26
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result1}, {puzzle2Result2}, {puzzle2Result3}, {puzzle2Result4}, {puzzle2Result5}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))