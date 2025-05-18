#import json

#employees = {"name":"gowri",
#             "father":"ramamoorthy",
#             "mother":"amutha",
#             "brother":"kavi"}

#file_path = "/Users/rgowrishankar/python project/examples.py/input.json"

#with open(file_path, "w") as file:
#    json.dump(employees, file)
#    print("file written")


import csv

employees = [["name", "age", "job"],
             ["gowri","27","devops"],
             ["nishanth", "24", "SRE"],
             ["sasi","33","developer"]]

file_path = "/Users/rgowrishankar/python project/examples.py/input.csv"

try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for x in employees:
            writer.writerow(x)
        print("file is written")
except FileExistsError:
    print("file already exists")
