class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property 
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property 
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("not valid")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("not valid")
    
rectangle1 = rectangle(3,4)
rectangle2 = rectangle(7,8)

rectangle1.width = 9
rectangle2.width = 6
rectangle1.height = 8
rectangle2.height = 6

print(rectangle1.width)
print(rectangle1.height)
print(rectangle2.height)
print(rectangle1.height)