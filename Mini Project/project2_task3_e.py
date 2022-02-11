import os
import argparse
import zipfile

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("src1", type=str)
parser.add_argument("src2", type=str)
parser.add_argument("dst", type=str)

args = parser.parse_args()

if os.path.exists(args.src1) or os.path.exists(args.src2):
    pass
else:
    print("The sources aren't correct")
    raise FileNotFoundError

if os.path.isdir(args.dst):
    pass
elif args.dst[-4:len(args.dst):1] == ".zip":
    pass
else:
    print("destination is wrong")
    raise FileNotFoundError
try:
    os.mkdir("new_archive")
except:
    pass
with zipfile.ZipFile(args.src1, "r") as file:
    file.extractall("new_archive")
with zipfile.ZipFile(args.src2, "r") as file:
    file.extractall("new_archive")
if os.path.isdir(args.dst):
    with zipfile.ZipFile(args.dst + "/new_archive.zip", "w") as file_write:
        for roots, directories, filings in os.walk("new_archive", topdown=False):
            for nickname in filings:
                file_write.write(roots + "/" + nickname)
            for nickname in directories:
                file_write.write(roots + "/" + nickname)
elif args.dst[-4:len(args.dst):1] == ".zip":
    with zipfile.ZipFile(args.dst, "w") as file_write:
        for roots, directories, filings in os.walk("new_archive", topdown=False):
            for nickname in filings:
                file_write.write(roots + "/" + nickname)
            for nickname in directories:
                file_write.write(roots + "/" + nickname)
