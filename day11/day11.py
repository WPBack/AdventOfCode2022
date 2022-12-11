# Import modules
import os
from termcolor import colored
import re

# Monkey class
class Monkey:
    def __init__(self, monkeyString):
        self.id = int(monkeyString[0][7])
        self.items = [int(num) for num in re.findall(r'\d+', monkeyString[1])]
        self.operation = monkeyString[2][23]
        self.operationArg = monkeyString[2][25:]
        self.testDivisable = int(monkeyString[3][21:])
        self.trueTarget = int(monkeyString[4][-1])
        self.falseTarget = int(monkeyString[5][-1])
        self.numInspected = 0

    def addItem(self, item):
        self.items.append(item)

    def playRound(self, monkeys):
        self.numInspected += len(self.items)
        for item in self.items:
            if self.operation == '*':
                if self.operationArg == 'old':
                    item *= item
                else:
                    item *= int(self.operationArg)
            else:
                if self.operationArg == 'old':
                    item += item
                else:
                    item += int(self.operationArg)

            item //= 3

            if item%self.testDivisable == 0:
                monkeys[self.trueTarget].addItem(item)
            else:
                monkeys[self.falseTarget].addItem(item)

        self.items = []

    def playRoundPart2(self, monkeys):
        self.numInspected += len(self.items)
        for item in self.items:
            if self.operation == '*':
                if self.operationArg == 'old':
                    item *= item
                else:
                    item *= int(self.operationArg)
            else:
                if self.operationArg == 'old':
                    item += item
                else:
                    item += int(self.operationArg)

            if item%self.testDivisable == 0:
                monkeys[self.trueTarget].addItem(item)
            else:
                monkeys[self.falseTarget].addItem(item)

        self.items = []


# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    lines = inputFile.read().splitlines()

    monkeys = []
    for lineId in range(0, len(lines), 7):
        monkeys.append(Monkey(lines[lineId:lineId+7]))

    # Close the file and return the result
    inputFile.close()
    return monkeys

# Puzzle 1
def puzzle1(filename):
    # Read file
    monkeys = input_parser(filename)
    
    # Play the game for 20 iterations
    for game in range(20):
        for monkey in monkeys:
            monkey.playRound(monkeys)

    # Return the multiplication of the most active monkeys
    sortedNumInspected = sorted([monkey.numInspected for monkey in monkeys])
    return sortedNumInspected[-1]*sortedNumInspected[-2]

# Puzzle 2
def puzzle2(filename):
    # Read file
    monkeys = input_parser(filename)
    
    # Play the game for 1000 iterations
    for game in range(1000):
        for monkey in monkeys:
            monkey.playRound(monkeys)
        print(f'Game {game} completed, {game/10}%')

    # Return the multiplication of the most active monkeys
    sortedNumInspected = sorted([monkey.numInspected for monkey in monkeys])
    return sortedNumInspected[-1]*sortedNumInspected[-2]

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 10605
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 1 FAIL, got {puzzle1Result}', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2Result = puzzle2('example1')
puzzle2TestPass = puzzle2Result == 2713310158
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored(f'Tests for puzzle 2 FAIL, got {puzzle2Result}', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))