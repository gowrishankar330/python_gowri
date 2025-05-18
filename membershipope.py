#word = "apple"
#letter = input("enter a word: ")
#if letter in word:
#    print(f"{letter} is there")
#else:
#    print(f"{letter} not found")



#students = ["gowri", "harish", "sasi", "prathap","shankar"]
#name = input("enter a student name: ")
#if name not in students:
#    print(f"{name} va apdi yaarum illayae")
#else:
#    print(f"{name} ah antha punda ulla than kedakum")


#grade = {"gowri":"A", "harish":"F", "sasi":"A+", "prathap":"E","BSD":"O"}
#students = input("enter the student name: ")
#if students not in grade:
#    print(f"{students} not found!")
#else:
#    print(f"{students}'s grade is {grade[students]}")


email = input("enter ur email: ")
if "@" in email and "." in email:
    print(f"{email} is valid")
else:
    print(f"{email} is not valid")