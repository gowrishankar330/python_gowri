#text_data= "i love pizza"

#file_path = "/Users/rgowrishankar/python project/output.txt"

#try:
#    with open(file_path, "a") as file:
#        file.write("\n" + text_data)
#        print(f"{text_data} is written to {file_path}")
#except FileExistsError:
#    print("already there")


employees = ["gowri", "shankar","sasi", "kumar", "harish", "appu"]

file_path = "/Users/rgowrishankar/python project/output.txt"

try:
    with open(file_path, "a") as file:
        for x in employees:
            file.write("\n" + x)
        print(f"{employees} is written to {file_path}")
except FileExistsError:
    print("already there")