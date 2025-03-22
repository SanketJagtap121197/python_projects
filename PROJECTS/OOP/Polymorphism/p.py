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

# Create instances
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Use polymorphism to call methods
print("Rectangle:")
print_shape_info(rectangle)

print("Circle:")
print_shape_info(circle)


'''
This code demonstrates polymorphism by defining a Shape base class with abstract methods, and two derived classes 
(Rectangle and Circle) that implement these methods. The print_shape_info() function accepts any Shape instance and
calls its methods, showcasing polymorphism. Let me know if you need modifications
'''

'''
How Polymorphism Works in Python OOP

Polymorphism is a key concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common base class. It enables a single interface to be used with different types of objects.

Key Aspects of Polymorphism:

Method Overriding – A child class provides a specific implementation of a method already defined in its parent class.

Method Overloading (Not native to Python) – Achieved using default arguments or *args/**kwargs.

Function/Operator Overloading – Python allows overloading certain operators using magic methods (like __add__, __str__).

How Polymorphism Works in Our Project

In the given Python project:

Base Class (Shape)

Defines two abstract methods: area() and perimeter(), but does not provide implementation.

Any subclass must implement these methods.

Derived Classes (Rectangle and Circle)

Both classes inherit from Shape and provide their own implementations of area() and perimeter().

The method names are the same across different classes, but their behavior is specific to each shape.

Using Polymorphism in the Function print_shape_info()

This function accepts any Shape object and calls area() and perimeter().

It works with both Rectangle and Circle objects without modification.
'''