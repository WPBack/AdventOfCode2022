# Import modules
import os
from termcolor import colored

# Class for a file
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

# Class for a directory
class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.children = []

    def add_file(self, file):
        self.files.append(file)

    def add_child(self, child):
        self.children.append(child)

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for child in self.children:
            size += child.get_size()
        return size

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    lines = inputFile.read().splitlines()

    # Create the root directory and add all the children and files
    root = Directory('/', None)
    currDir = root

    for line in lines[1:]:
        if line[0] == '$':
            if line[2:7] == 'cd ..':
                currDir = currDir.parent

            elif line[2:4] == 'cd':
                for child in currDir.children:
                    if child.name == line[5:]:
                        currDir = child
                        break

        elif line[0:3] == 'dir':
            currDir.add_child(Directory(line[4:], currDir))

        else:
            file = line.split(' ')
            currDir.add_file(File(file[1], int(file[0])))

    # Close the file and return the result
    inputFile.close()
    return root

# Recursive helper (that calls recursive function :O) that gets the sum of small directories
def get_sum_of_small_dirs(dir):
    size = dir.get_size()
    if size > 100000:
        size = 0
    for child in dir.children:
        size += get_sum_of_small_dirs(child)
    return size


# Puzzle 1
def puzzle1(filename):
    # Read file
    root = input_parser(filename)
    
    return get_sum_of_small_dirs(root)

# Puzzle 2
def puzzle2(filename):
    # Read file
    inputs = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1Result = puzzle1('example1')
puzzle1TestPass = puzzle1Result == 95437
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