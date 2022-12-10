# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    lines = inputFile.read().splitlines()

    # Close the file and return the result
    inputFile.close()
    return lines

# Puzzle 1
def puzzle1(filename):
    # Read file
    lines = input_parser(filename)

    # Create a set of all positions the tail has visitet
    visited = set([(0,0)])

    # Simulate the movement
    headPos = (0,0)
    tailPos = (0,0)
    for line in lines:
        for i in range(int(line[2:])):
            oldHeadPos = headPos
            if line[0] == 'R':
                headPos = (headPos[0]+1, headPos[1])
                if headPos[0] - tailPos[0] > 1:
                    tailPos = oldHeadPos

            elif line[0] == 'L':
                headPos = (headPos[0]-1, headPos[1])
                if tailPos[0] - headPos[0] > 1:
                    tailPos = oldHeadPos

            elif line[0] == 'U':
                headPos = (headPos[0], headPos[1]-1)
                if tailPos[1] - headPos[1] > 1:
                    tailPos = oldHeadPos

            elif line[0] == 'D':
                headPos = (headPos[0], headPos[1]+1)
                if headPos[1] - tailPos[1] > 1:
                    tailPos = oldHeadPos

            visited.add(tailPos)

    return len(visited)

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 13
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2Result = puzzle2('example1')
puzzle2TestPass = puzzle2Result == 2
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))