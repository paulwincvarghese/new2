from abc import abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
    
r=Rectangle(4,5)
c=Circle(3)
s=Square(4)

print("Area of Rectangle:", r.area())
print("Area of Circle:", c.area())
print("Area of Square:", s.area())
    