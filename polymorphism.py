import math
class shape:
    def __init__(self,colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"its an {self.colour} and its {'filled' if self.is_filled else 'not filled'}")


class circle(shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"it is ac circle with area of {math.pi * self.radius * self.radius}")
        

class square(shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"it is an square with area of {self.width * self.width}")

class triangle(shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"it is an triangle with area of {0.5* self.width * self.height}")

class food(circle):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled,radius)
        super().describe()



shapes = [circle("red", True, 5), square("blue", True, 10), triangle("green", False, 8, 9), food("red", False,4)]

for x in shapes:
    x.describe()
    print()


