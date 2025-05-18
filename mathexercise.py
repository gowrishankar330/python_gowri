import math
circle = float(input("enter the radius of the circle: "))
circumference = 2 * math.pi * circle
radius = float(input("enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print(f" the area of circle is: {round(circumference, 4)}")
print(f" the fullarea of circle is: {round(area, 1)}")