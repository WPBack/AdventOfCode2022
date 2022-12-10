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
def sign(integer):
    if integer == 0:
        return 0
    else:
        return int(integer/abs(integer))

def puzzle2(filename):
    # Read file
    lines = input_parser(filename)

    # Create a set of all positions the tail has visitet
    visited = set([(0,0)])

    # Simulate the movement
    snake = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    for line in lines:
        for i in range(int(line[2:])):
            if line[0] == 'R':
                snake[0] = (snake[0][0]+1, snake[0][1])
            elif line[0] == 'L':
                snake[0] = (snake[0][0]-1, snake[0][1])
            elif line[0] == 'U':
                snake[0] = (snake[0][0], snake[0][1]+1)
            elif line[0] == 'D':
                snake[0] = (snake[0][0], snake[0][1]-1)

            for ropeId in range(9):
                if abs(snake[ropeId+1][0] - snake[ropeId][0]) > 1 or abs(snake[ropeId+1][1] - snake[ropeId][1]) > 1:
                    snake[ropeId+1] = (snake[ropeId+1][0] + sign(snake[ropeId][0] - snake[ropeId+1][0]), snake[ropeId+1][1] + sign(snake[ropeId][1] - snake[ropeId+1][1]))
                

            visited.add(snake[9])

    return len(visited)

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
puzzle2Result1 = puzzle2('example1')
puzzle2Result2 = puzzle2('example2')
puzzle2TestPass = puzzle2Result1 == 1 and puzzle2Result2 == 36
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result1}, {puzzle2Result2}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))