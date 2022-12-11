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

    x = 1
    signalStrengthSum = 0
    cycle = 1
    cyclesLeftOnInstruction = 0
    for line in lines:
        if line[0:4] == 'noop':
            cyclesLeftOnInstruction = 0
        elif line[0:4] == 'addx':
            cyclesLeftOnInstruction = 1

        for i in range(cyclesLeftOnInstruction+1):
            if (cycle-20) % 40 == 0:
                signalStrengthSum += cycle*x
            cycle += 1

        if line[0:4] == 'addx':
            x += int(line[5:])

    return signalStrengthSum

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1Result0 = puzzle1('example0')
puzzle1Result1 = puzzle1('example1')
puzzle1TestPass = puzzle1Result0 == 0 and puzzle1Result1 == 13140
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result0}, {puzzle1Result1}', 'red'))

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