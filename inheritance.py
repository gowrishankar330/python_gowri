class cricket:
    def __init__(self, name, country, colour,charity):
        self.name = name
        self.country = country
        self.colour = colour
        self.charity = charity
        is_champions = True

    def name_of_franchise(self):
        print(f"yes they are {self.name} ")
    
    def place(self):
        print(f"they are from {self.country}")
    
class chennai(cricket):
    def colour_of_frachise(self):
        print(f"they are {self.colour} ")

    def charity_jersey(self):
        print(f"they are {self.charity} ")

class kolkata(cricket):
    def colour_of_frachise(self):
        print(f"they are {self.colour} ")

    def charity_jersey(self):
        print(f"they are {self.charity} ")

class bangalore(cricket):
    def colour_of_frachise(self):
        print(f"they are {self.colour} ")

    def charity_jersey(self):
        print(f"they are {self.charity} ")

chennai_team = chennai("CSK","india", "yellow", "green")
kolkata_team = kolkata("KKR", "india", "black", "yellow")
bangalore_team = bangalore("RCB", "india", "red", "orange")

print("------------------------")
kolkata_team.name_of_franchise()
kolkata_team.colour_of_frachise()
kolkata_team.charity_jersey()
kolkata_team.place()
print("------------------------")
bangalore_team.name_of_franchise()
bangalore_team.colour_of_frachise()
bangalore_team.charity_jersey()
bangalore_team.place()
print("------------------------")
chennai_team.name_of_franchise()
chennai_team.colour_of_frachise()
chennai_team.charity_jersey()
chennai_team.place()