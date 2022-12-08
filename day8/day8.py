# Import modules
import os
from termcolor import colored
import numpy as np

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    trees = [[int(char) for char in line] for line in inputFile.read().splitlines()]

    # Close the file and return the result
    inputFile.close()
    return trees

# Puzzle 1
def puzzle1(filename):
    # Read file
    trees = input_parser(filename)

    # Create boolean map of visible trees
    visibleTrees = [[False for j in range(len(trees[0]))] for i in range(len(trees))]
    
    # Look from the left and right
    for row in range(len(trees)):
        maxHeightFromLeft = -1
        maxHeightFromRight = -1
        for col in range(len(trees[0])):
            if trees[row][col] > maxHeightFromLeft:
                visibleTrees[row][col] = True
                maxHeightFromLeft = trees[row][col]

            if trees[row][len(trees[0]) - col - 1] > maxHeightFromRight:
                visibleTrees[row][len(trees[0]) - col - 1] = True
                maxHeightFromRight = trees[row][len(trees[0]) - col - 1]

    # Look from the top and bottom
    for col in range(len(trees[0])):
        maxHeightFromTop = -1
        maxHeightFromBottom = -1
        for row in range(len(trees)):
            if trees[row][col] > maxHeightFromTop:
                visibleTrees[row][col] = True
                maxHeightFromTop = trees[row][col]

            if trees[len(trees) - row - 1][col] > maxHeightFromBottom:
                visibleTrees[len(trees) - row - 1][col] = True
                maxHeightFromBottom = trees[len(trees) - row - 1][col]

    # Count the number of visible trees
    nrVisible = 0
    for row in range(len(trees)):
        for col in range(len(trees[0])):
            if visibleTrees[row][col]:
                nrVisible += 1

    return nrVisible

# Puzzle 2
def puzzle2(filename):
    # Read file
    trees = np.array(input_parser(filename))

    # Find the most scenic spot
    mostScenic = 0
    for row in range(1, len(trees)-1):
        for col in range(1, len(trees[0])-1):
            height = trees[row, col]
            viewDown = 0
            canSeeDown = True
            viewUp = 0
            canSeeUp = True
            viewRight = 0
            canSeeRight = True
            viewLeft = 0
            canSeeLeft = True

            # Look down
            for tree in trees[row+1:len(trees), col]:
                if canSeeDown:
                    viewDown += 1
                if tree >= height:
                    canSeeDown = False

            # Look up
            for tree in reversed(trees[0:row, col]):
                if canSeeUp:
                    viewUp += 1
                if tree >= height:
                    canSeeUp = False

            # Look right
            for tree in trees[row, col+1:len(trees[0])]:
                if canSeeRight:
                    viewRight += 1
                if tree >= height:
                    canSeeRight = False

            # Look left
            for tree in reversed(trees[row, 0:col]):
                if canSeeLeft:
                    viewLeft += 1
                if tree >= height:
                    canSeeLeft = False
        
            # Update highscore
            score = viewDown*viewUp*viewRight*viewLeft
            if score > mostScenic:
                mostScenic = score

    return mostScenic

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 21
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2Result = puzzle2('example1')
puzzle2TestPass = puzzle2Result == 8
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))