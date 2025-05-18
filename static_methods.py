class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def state(self):
        print(f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_positions(position):
        valid_position =["support", "SRE", "DEVOPS", "manager"]
        if position in valid_position:
                return "its! there"
        else:
                return "its not there"
    
employee1 = employee("gowri","support")
employee2 = employee("nishanth", "SRE")
employee3 = employee("BSD", "DEVOPS")
employee4 = employee("sabir","manager")

employee1.state()
employee2.state()
employee3.state()
employee4.state()
print(employee4.is_valid_positions("docker"))