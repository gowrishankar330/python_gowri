class animal:
    def __init__(self, name , size):
        self.name = name
        self.size = size
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
class hunter(animal):
    
    def hunt(self):
        print(f"{self.name} is hunting")

class prey(animal):

    def eaten(self):
        print(f"{self.name} is being eaten")

class catfamily(hunter):

    def catsfamily(self):
        print(f"{self.name} is hunting")
        print(f"{self.size} in size")

class preyfamily(prey):

    def preysfamily(self):
        print(f"{self.name} is being eaten")
        print(f"{self.size} in size ")

class fishes(hunter, prey):
    def fish(self):
        print(f"{self.name} can do both also being {self.size} matters")


lioness = hunter("tiger", "muscled")
elephant = fishes("elephants", "gigantic")
mouse = prey("Mouse", "small")
rhino = catfamily("Rhino","big")
cats = preyfamily("Cat", "quite small")


lioness.hunt()
elephant.fish()
mouse.eaten()
rhino.catsfamily()
cats.preysfamily()
cats.eaten()
cats.eat()
cats.sleep()
elephant.eaten()