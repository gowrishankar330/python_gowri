class car:
    def __init__(self, model, price, year, fuel):
        self.model = model
        self.price = price
        self.year = year
        self.fuel = fuel

car1 = car("maruthi x5", "5lakhs", 2015, "diesel")
car2 = car("maruthi x6", "10lakhs", 2024, "petrol")
print(car1.model)
print(car1.price)
print(car1.fuel)
print(car2.model)
print(car2.price)
print(car2.fuel)