#file_path = "/Users/rgowrishankar/python project/output.txt"
#try:
#    with open(file_path, "r") as file:
#        content = file.read()
#        print(content)
#except FileNotFoundError:
#    print("file doesnt exists")

import json
import csv
file_path = "/Users/rgowrishankar/python project/examples.py/input.csv"
try:
    with open(file_path, "r") as file:
       # content = json.load(file)
         content = csv.reader(file)
         for x in content:
             print("\n", x[2])
except FileNotFoundError:
    print("file doesnt exists")