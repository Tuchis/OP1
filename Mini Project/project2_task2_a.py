from os import walk
import argparse

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("path", type=str)

args = parser.parse_args()
f = []
start_path = args.path

def branch_create(file):
    """
    Creates tuples of the pathes
    """
    for (dirpath, dirnames, filenames) in walk(file):
        filenames_new = []
        for elem in filenames:
            filenames_new.append(file + "/" + elem)
        f = tuple(filenames_new)
        dirnames = tuple(dirnames)
        dir_branches = ()
        for directory in dirnames:
            path = file + "/" + directory
            in_dir = branch_create(path)
            directory = (path, in_dir)
            dir_branches += directory
        dir_branches += f
        return (dir_branches)



def branch_drawer(pathes):
    # draws the tree of
    try:
        for directory in pathes:
            if isinstance(directory, tuple):
                branch_drawer(directory)
            if isinstance(directory, str):
                directory_new = directory.split("/")
                if directory == pathes[-1]:
                    print("│  " * (len(directory_new) - 2) + "└── " + directory_new[-1], end="")
                elif directory == pathes[-2] and isinstance(pathes[-1], tuple):
                    print("│  " * (len(directory_new) - 2) + "└── " + directory_new[-1], end="")
                else:
                    print("│  " * (len(directory_new) - 2) + "├── " + directory_new[-1], end="")
                try:
                    if isinstance(pathes[pathes.index(directory) + 1], tuple) and pathes[pathes.index(directory) + 1] != ():
                        print("/")
                    else:
                        print("")
                except:
                    print()
    except:
        print("The wrong folder")
        raise FileNotFoundError

print("./")
branch_drawer((branch_create(start_path)))
