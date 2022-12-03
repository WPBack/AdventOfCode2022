# Import modules
import os
from termcolor import colored

# Helper to convert character into priority
def get_prio(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    lines = inputFile.read().splitlines()

    rucksacks = []
    for line in lines:
        compartment1 = [get_prio(item) for item in line[:len(line)//2]]
        compartment2 = [get_prio(item) for item in line[len(line)//2:]]
        rucksacks.append((compartment1, compartment2))

    # Close the file and return the result
    inputFile.close()
    return rucksacks

# Puzzle 1
def puzzle1(filename):
    # Read file
    rucksacks = input_parser(filename)

    return sum([set(rucksack[0]).intersection(rucksack[1]).pop() for rucksack in rucksacks])

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 157
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