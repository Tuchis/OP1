import os
import argparse
import re

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("line", type=str)
parser.add_argument("src", type=str)

#Optional argument
parser.add_argument("--show_lines", action="store_true")
parser.add_argument("--only_show_counts", action="store_true")

args = parser.parse_args()

if os.path.isdir(args.src):
    pass
else:
    print("The folder isn't correct")
    raise FileNotFoundError

matches = 0
outputs = []
for (dirpath, dirnames, filenames) in os.walk(args.src):
    for name in filenames:
        if re.search(args.line, name):
            output = [name]
            matches += 1
            with open(args.src + "/" + name, "r") as filer:
                counter = 1
                for i in filer:
                    output.append((i, counter))
                    counter += 1
            outputs.append(output)
if args.show_lines is True:
    for elem in outputs:
        for line in elem:
            if isinstance(line, str):
                print(line)
            else:
                print(str(line[1])+": "+line[0], end = "")
        if elem != outputs[-1]:
            print("\n")
elif args.only_show_counts is True:
    print(matches)
else:
    for elem in outputs:
        print(elem[0])
        for x in elem[1:]:
            print(x[0], end="")
        if elem != outputs[-1]:
            print("\n")
        else:
            print("\n\n\n")