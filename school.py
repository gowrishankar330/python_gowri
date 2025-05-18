class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class Student(Person):
    def __init__(self, name, age, sport, student_id):
        super().__init__(name, age)
        self.sport = sport
        self.student_id = student_id
        self.grades = []

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old & im a {self.sport} player")

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class Teacher(Person):
    def __init__(self, name, age, sex, subject):
        super().__init__(name, age)
        self.subject = subject
        self.sex = sex
    def greet_teacher(self):
        print(f"My teacher is {self.name} who is {self.age} years old")
    def teach(self):
        if self.sex == "male":
          print(f"he is teaching {self.subject}.")
        else:
          print(f"she is teaching {self.subject}.")

# A regular function outside of any class
def welcome_message():
    print("Welcome to the School System!\n")

# Main function to run the program
def main():
    welcome_message()

    # Create a student and a teacher
    student1 = Student("Alice", 16, "football", "S122")
    teacher1 = Teacher("Mr. Smith", 45, "male", "Math")
    teacher2 = Teacher("Mrs. Smith", 45, "female", "Math")

    # Interactions
    student1.greet()
    student1.add_grade(88)
    student1.add_grade(92)
    print(f"{student1.name}'s average grade is: {student1.average_grade()}")

    print()

    teacher2.greet_teacher()
    #teacher1.teach()
    teacher2.teach()

# Entry point
if __name__ == "__main__":
    main()