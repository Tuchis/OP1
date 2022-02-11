"""
Project 2 Task 1 B
"""

import argparse

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("switched_string", type=str)
parser.add_argument("switching_string", type=str)
parser.add_argument("path", type=str)

#Optional argument
parser.add_argument("--inplace", action="store_true")

args = parser.parse_args()


def reader(path, switched, switching):
    """
    The function to read the file and find the lines to switch
    """
    try:
        changed_file = ""
        with open(path, "r+") as file:
            for line in file:
                line = line.replace(switched, switching)
                changed_file += line
        return changed_file
    except FileNotFoundError:
        print("The file path is not correct")
        return None

def inplace_fact(changes, fact):
    """
    The function, that prints or rewrites file
    """
    if changes is None:
        return None
    if fact is True:
        with open(args.path, "w") as file:
            file.write(changes)
    else:
        print(changes)

inplace_fact(reader(args.path, args.switched_string, args.switching_string), args.inplace)
