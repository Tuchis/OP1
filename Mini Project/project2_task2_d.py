import os
import argparse

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("src", type=str)
parser.add_argument("dst", type=str)

args = parser.parse_args()

if os.path.exists(args.src):
    pass
else:
    print("Source file isn't correct")
    raise FileNotFoundError
if os.path.exists(args.dst):
    pass
else:
    try:
        os.mkdir(args.dst)
    except:
        print("The path to the folder isn't correct")
        raise FileNotFoundError

os.rename(args.src, args.dst + "/" + os.path.basename(args.src))
