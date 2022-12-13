# Import modules
import os
from termcolor import colored
import ast

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    lines = inputFile.read().splitlines()
    packets = []
    for line in lines:
        if line != '':
            packets.append(ast.literal_eval(line))

    # Close the file and return the result
    inputFile.close()
    return packets

def right_order(left, right):

    if type(left) == int and type(right) == int:
        if right > left:
            return True
        elif left > right:
            return False

    else:
        if type(left) == int:
            left_list = [left]
        else:
            left_list = left
        if type(right) == int:
            right_list = [right]
        else:
            right_list = right
        for i in range(min(len(left_list), len(right_list))):
            res = right_order(left_list[i], right_list[i])
            if not res is None:
                return res
        if len(left_list) < len(right_list):
            return True
        elif len(right_list) < len(left_list):
            return False
        else:
            return None

# Puzzle 1
def puzzle1(filename):
    # Read file
    packets = input_parser(filename)

    sumOfIndices = 0
    for i in range(0, len(packets), 2):
        if right_order(packets[i], packets[i+1]):
            sumOfIndices += i/2+1

    return sumOfIndices

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