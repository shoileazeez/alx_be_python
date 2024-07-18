from math import pi
class Shape:
    def area(self, good):
        self.good = good 
        raise NotImplementedError
    
    
class Rectangle(Shape):
    def area(self, length, width):
        super().area()
        self.length = length
        self.width = width
        self.area = length * width
        return "The area of the Rectangle is: " +self.area
    
    
    
class Circle(Shape):
    def area (self, radius):
        super().area()
        self.radius = radius
        self.area = pi * +self.radius **2 
        return "The area of the Circle is: " + self.area
     
     
     
     
Rectangle.area()
Circle.area()
Shape = Rectangle(Circle())   