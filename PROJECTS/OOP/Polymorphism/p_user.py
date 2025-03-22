# Polymorphism in OOP using Python

# Base class: Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Assign width
        self.height = height  # Assign height

    def area(self):
        return self.width * self.height  # Calculate area of rectangle

    def perimeter(self):
        return 2 * (self.width + self.height)  # Calculate perimeter of rectangle

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Assign radius

    def area(self):
        return 3.14 * self.radius * self.radius  # Calculate area of circle

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Calculate perimeter of circle

# Function to demonstrate polymorphism
def print_shape_info(shape):
    print(f"Area: {shape.area()}")  # Call area method
    print(f"Perimeter: {shape.perimeter()}")  # Call perimeter method
    print("---------------------")

# User input for Rectangle
width = float(input("Enter width of the rectangle: "))
height = float(input("Enter height of the rectangle: "))
rectangle = Rectangle(width, height)

# User input for Circle
radius = float(input("Enter radius of the circle: "))
circle = Circle(radius)

# Use polymorphism to call methods
print("Rectangle:")
print_shape_info(rectangle)

print("Circle:")
print_shape_info(circle)