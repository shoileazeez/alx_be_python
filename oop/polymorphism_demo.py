class Shape:
    def area(self): 
        raise NotImplementedError
    
    def description(self):
        return "This is a shape"
    
    
class Rectangle(Shape):
    def __init__(self, length ,width):
        # super().__init__()
        self.width = width
        self.length  = length 
        
        
    def area(self):
        return self.length * self.width
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
        
    def area(self):
        import math
        return math.pi * self.radius ** 2    
        
          
    
    # def description(self):
    #     return"This is a rectangle"
    
    
# def print_shape_info(shape):
#     print(shape.description())
#     print(f"Area: {shape.area()}") 
    
    
# rect = Rectangle(4, 5)

# print_shape_info(rect)
    

    # def area (self, radius):
    #     super().area()
    #     self.radius = radius
    #     self.area = pi * +self.radius **2 
    #     return "The area of the Circle is: " + self.area
     
     
     
     
