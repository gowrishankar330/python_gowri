class car:
    def __init__(self, model, price, year, fuel):
        self.model = model
        self.price = price
        self.year = year
        self.fuel = fuel

    def drive(self):
        print(f"you drive the {self.model} which is {self.price} worth & its a {self.fuel} engine")
    def stop(self):
        print(f"you stop the car whic was founded in {self.year}")
