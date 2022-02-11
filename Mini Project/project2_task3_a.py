import os
import argparse
import re
import zipfile

parser = argparse.ArgumentParser()

#Necessary args
parser.add_argument("line", type=str)
parser.add_argument("src", type=str)
parser.add_argument("dst", type=str)

args = parser.parse_args()

# opening Zip using 'with' keyword in read mode
with zipfile.ZipFile(args.src, 'r') as file:
    info = file.namelist()
    file.extractall()

if args.src[-4:len(args.src)] == ".zip":
    pass
else:
    print("Wrong archive")
    raise FileNotFoundError

if os.path.isdir(args.dst):
    pass
elif args.dst[-4:len(args.src)] == ".zip":
    pass
else:
    print("Wrong destination")
    raise FileNotFoundError

def search_for_files(info):
    try:
        os.mkdir("archive_not_copy_not_plag")
    except:
        pass
    files_to_del = []
    for elem in info:
        if elem[-1] == "/":
            pass
        else:
            if re.search(args.line, os.path.basename(elem)):
                files_to_del.append(elem)
            else:
                pass
    print(files_to_del)
    names = []
    for elem in files_to_del:
        os.rename(elem, "archive_not_copy_not_plag/" + os.path.basename(elem))
        names.append("archive_not_copy_not_plag/" + os.path.basename(elem))
        info.remove(elem)
    while len(info) > 0:
        for elem in info:
            try:
                os.rmdir(elem)
                info.remove(elem)
            except:
                try:
                    os.remove(elem)
                    info.remove(elem)
                except:
                    pass
    print(names)
    return names

names = search_for_files(info)

if args.dst[-4:len(args.dst):1] == ".zip":
    with zipfile.ZipFile(args.dst, 'w') as file:
        for elem in names:
            try:
                file.write(elem, os.path.basename(elem))
            except:
                pass
else:
    with zipfile.ZipFile(args.dst + "/" + os.path.basename(args.src), 'w') as file:
        for elem in names:
            try:
                file.write(elem, os.path.basename(elem))
            except:
                pass

def directory_delete(folder):
    for roots, directories, filings in os.walk(folder, topdown=False):
        for nickname in filings:
            os.remove(os.path.join(roots, nickname))
        for nickname in directories:
            os.rmdir(os.path.join(roots, nickname))
    if os.path.exists(folder):
        os.rmdir(folder)
directory_delete("archive_not_copy_not_plag")