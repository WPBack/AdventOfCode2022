# Import modules
import os
from termcolor import colored
import re

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    #lines = [re.findall(r'\d+', line) for line in inputFile.read().splitlines()]
    lines = [[int(char) for char in re.findall(r'\d+', line)] for line in inputFile.read().splitlines()]

    # Close the file and return the result
    inputFile.close()
    return lines

# Puzzle 1
def puzzle1(filename):
    # Read file
    inputs = input_parser(filename)
    
    result = 0
    for pair in inputs:
        if (pair[0] <= pair[2] and pair[1] >= pair[3]) or (pair[2] <= pair[0] and pair[3] >= pair[1]):
            result += 1

    return result

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)
    
    result = 0
    for pair in inputs:
        if (pair[0] <= pair[2] and pair[1] >= pair[2]) or (pair[2] <= pair[0] and pair[3] >= pair[0]):
            result += 1

    return result

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 2
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2Result = puzzle2('example1')
puzzle2TestPass = puzzle2Result == 4
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))