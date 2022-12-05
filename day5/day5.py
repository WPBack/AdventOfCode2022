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
    lines = inputFile.read().splitlines()

    # Find the number of stacks and maximum height
    maxHeight = 0
    done = False
    for line in lines:
        if len(line) > 1 and line[1] == '1':
            done = True
            nrStacks = int(re.findall(r'\d+', line)[-1])
        if not done:
            maxHeight += 1

    # Create stacks, lowest index at the bottom
    stacks = []
    for stackId in range(nrStacks):
        stacks.append([])
        for level in range(maxHeight):
            if lines[maxHeight-level-1][stackId*4+1] != ' ':
                stacks[stackId].append(lines[maxHeight-level-1][stackId*4+1])

    # Create list of instructions
    instructions = []
    for line in lines:
        if len(line) > 0 and line[0] == 'm':
            instructions.append([int(num) for num in re.findall(r'\d+', line)])

    # Close the file and return the result
    inputFile.close()
    return (stacks, instructions)

# Puzzle 1
def puzzle1(filename):
    # Read file
    (stacks, instructions) = input_parser(filename)

    # Perform the instructions
    for instruction in instructions:
        for numberToMove in range(instruction[0]):
            stacks[instruction[2]-1].append(stacks[instruction[1]-1].pop())

    # Put together the result
    result = ''
    for stack in stacks:
        result += stack.pop()
    return result

# Puzzle 2
def puzzle2(filename):
    # Read file
    (stacks, instructions) = input_parser(filename)

    # Perform the instructions
    for instruction in instructions:
        stacks[instruction[2]-1].extend(stacks[instruction[1]-1][-instruction[0]:])
        del stacks[instruction[1]-1][-instruction[0]:]

    # Put together the result
    result = ''
    for stack in stacks:
        result += stack.pop()
    return result

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 'CMZ'
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2Result = puzzle2('example1')
puzzle2TestPass = puzzle2Result == 'MCD'
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))