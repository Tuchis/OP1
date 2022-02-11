"""
Project 2 Task 1 B
"""

import argparse
import os.path

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("src_one", type=str)
parser.add_argument("src_two", type=str)
parser.add_argument("dst", type=str)

args = parser.parse_args()

def reader(source_one, source_two):
    """
    The function to read the file and find the lines to switch
    """
    try:
        common_lines = ""
        with open(source_one, "r") as file_one:
            for line in file_one:
                try:
                    with open(source_two, "r") as file_two:
                        for line_check in file_two:
                            if line == line_check:
                                common_lines += line
                                break
                except FileNotFoundError:
                    print("The file path is not correct")
                    return None
        return common_lines
    except FileNotFoundError:
        print("The file path is not correct")
        return None

def destination_write(dst, commons):
    """
    The function, that prints or rewrites file
    """
    if commons is None:
        return None
    if os.path.isdir(dst):
        print("Error, the destination is an folder")
        return None
    if os.path.exists(dst):
        print("Error, the file exists")
        return None
    try:
        with open(dst, "w") as file:
            file.write(commons)
    except:
        print("Error, the destination is not correct")

destination_write(args.dst, reader(args.src_one, args.src_two))