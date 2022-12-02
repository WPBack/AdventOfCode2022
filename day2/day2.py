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
    games = []
    for line in lines:
        if line[0] == 'A':
            opponent = 'rock'
        elif line[0] == 'B':
            opponent = 'paper'
        else:
            opponent = 'sissors'

        if line[2] == 'X':
            me = 'rock'
        elif line[2] == 'Y':
            me = 'paper'
        else:
            me = 'sissors'

        games.append((opponent, me))

    # Close the file and return the result
    inputFile.close()
    return games

# Helper to get the game result
def play(game):
    if game[0] == 'rock':
        if game[1] == 'rock':
            return 'draw'
        elif game[1] == 'paper':
            return 'win'
        else:
            return 'loss'
    elif game[0] == 'paper':
        if game[1] == 'rock':
            return 'loss'
        elif game[1] == 'paper':
            return 'draw'
        else:
            return 'win'
    else:
        if game[1] == 'rock':
            return 'win'
        elif game[1] == 'paper':
            return 'loss'
        else:
            return 'draw'

# Puzzle 1
def puzzle1(filename):
    # Read file
    games = input_parser(filename)

    points = 0
    for game in games:
        result = play(game)
        if result == 'win':
            points += 6
        elif result == 'draw':
            points += 3
        
        if game[1] == 'rock':
            points += 1
        elif game[1] == 'paper':
            points += 2
        else:
            points += 3

    return points

# Puzzle 2
def puzzle2(filename):
    # Read file
    games = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 15
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 2
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))