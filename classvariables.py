class student:

    from_place = "karaikudi"
    num_of_studets = 0

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour
        student.num_of_studets += 1

student1 = student("gandhi", 16 , "orange")
student2 = student("harish", 12, "pink")
student3 = student("nirmal", 13, "green")

#print(student.from_place)
#print(student2.age)
#print(student2.from_place)
#print(student3.colour)
#print(student2.from_place)
#print(student.num_of_studets)

print(f"my class has {student.num_of_studets} students from {student.from_place}")
