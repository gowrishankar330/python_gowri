import os

file_path = "/Users/rgowrishankar/python project"

if os.path.exists(file_path):
    print(f"you file is {file_path}")
    if os.path.isfile(file_path):
        print("its an file")
    elif os.path.isdir(file_path):
        print("its an folder")
else:
    print("file doesnt exits")