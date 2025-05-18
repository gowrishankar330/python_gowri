class employee:
    count = 0
    total_salary = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.count += 1
        employee.total_salary += salary

    def state(self):
        print(f"{self.name} = {self.salary}")

    @classmethod
    def get_count(cls):
        return f"total employee's: {cls.count}"

    @classmethod
    def get_salary_ave(cls):
        if employee.count == 0:
            return 0
        else:
            return f"average salary of employee is {cls.total_salary /cls.count} per year"
            
employee1 = employee("gowri", 45000)
employee2 = employee("nishanth", 100000)
employee3 = employee("BSD", 200000)
employee4 = employee("sabir", 150000)

print(employee.state(employee1))
print(employee.get_count())
print(employee.count)
print(employee.get_salary_ave())

