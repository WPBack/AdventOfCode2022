# Import modules
import os
from termcolor import colored
import numpy as np
import sys
import matplotlib.pylab as plt

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    lines = inputFile.read().splitlines()
    startPos = (0,0)
    goalPos = (0,0)
    map = []
    for row in range(len(lines)):
        map.append([])
        for col in range(len(lines[0])):
            if lines[row][col] == 'S':
                startPos = (row, col)
                map[row].append(0)
            elif lines[row][col] == 'E':
                goalPos = (row, col)
                map[row].append(25)
            else:
                map[row].append(ord(lines[row][col]) - 97)

    # Close the file and return the result
    inputFile.close()
    return (startPos, goalPos, np.matrix(map))

# Recursive function to find the cheapest path
def cheapest_path(pos, goal, cost, map, costMap):
    # Check if we have found a cheaper path, if not return
    if cost < costMap[pos]:
        costMap[pos] = cost
    else:
        return

    # Check if we have reached the goal, if so return
    if pos == goal:
        return

    # Check all directions
    if pos[0] > 0 and map[(pos[0]-1, pos[1])]-map[pos] <= 1: # up
        cheapest_path((pos[0]-1, pos[1]), goal, cost+1, map, costMap)
    if pos[1] < map.shape[1]-1 and map[(pos[0], pos[1]+1)]-map[pos] <= 1: # right
        cheapest_path((pos[0], pos[1]+1), goal, cost+1, map, costMap)
    if pos[0] < map.shape[0]-1 and map[(pos[0]+1, pos[1])]-map[pos] <= 1: # down
        cheapest_path((pos[0]+1, pos[1]), goal, cost+1, map, costMap)
    if pos[1] > 0 and map[(pos[0], pos[1]-1)]-map[pos] <= 1: # left
        cheapest_path((pos[0], pos[1]-1), goal, cost+1, map, costMap)

# Puzzle 1
def puzzle1(filename):
    # Read file
    (pos, goal, map) = input_parser(filename)
    costMap = np.matrix(np.ones(map.shape) * np.inf)
    
    sys.setrecursionlimit(10000)
    cheapest_path(pos, goal, 0, map, costMap)

    return costMap[goal]

# Puzzle 2
def puzzle2(filename):
    # Read file
    (pos, goal, map) = input_parser(filename)
    costMap = np.matrix(np.ones(map.shape) * np.inf)

    sys.setrecursionlimit(10000)
    progress = 0
    for row in range(map.shape[0]):
        for col in range(map.shape[1]):
            if map[row, col] == 0:
                cheapest_path((row, col), goal, 0, map, costMap)
            progress += 1
            print(f'{progress*100/map.size}%')

    return costMap[goal]

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 31
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input'))) # Commented out to save time

# Run tests for puzzle 2
puzzle2Result = puzzle2('example1')
puzzle2TestPass = puzzle2Result == 29
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))