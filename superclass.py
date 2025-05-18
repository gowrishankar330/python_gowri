import math
class shape:
    def __init__(self,colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"its an {self.colour} and its {"filled" if self.is_filled else "not filled"}")


class circle(shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        # self.colour = 'black'
        self.radius = radius

    def print_examples(self):
        print("tyre, Bangle")

    # def describe(self):
    #     super().describe()
    #     print(f"it is ac circle with area of {math.pi * self.radius * self.radius}")
        

class square(shape):
    def __init__(self, colour, is_filled, width):
        # super().__init__(colour, is_filled)
        self.width = width
    def describe(self):
        # super().describe()
        print(f"it is an square with area of {self.width * self.width}")

class triangle(shape):
    def __init__(self, colour, is_filled, width, height):
        # super().__init__(colour, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        # super().describe()
        print(f"it is an triangle with area of {0.5* self.width * self.height}")

circle_reading = circle("red", True, 5)
# square_reading = square("blue", True, 10)
# triangle_reading= triangle("green", False, 8, 9)


#print(circle_reading.colour)
#print(triangle_reading.height)
#print(square_reading.is_filled)
circle_reading.describe()
circle_reading.print_examples()
# triangle_reading.describe()
# square_reading.describe()