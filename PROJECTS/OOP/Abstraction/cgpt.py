from abc import ABC, abstractmethod  # Import required modules

# Abstract class defining a Shape
class Shape(ABC):
    @abstractmethod  # This forces subclasses to implement this method
    def area(self):
        pass  # No implementation here, subclasses must provide it

    @abstractmethod
    def perimeter(self):
        pass  # No implementation here, subclasses must provide it

# Concrete subclass of Shape (must implement the abstract methods)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius

    def area(self):  # Implementing the abstract method
        return 3.14 * self.radius * self.radius

    def perimeter(self):  # Implementing the abstract method
        return 2 * 3.14 * self.radius

# Concrete subclass of Shape (must implement the abstract methods)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Implementing the abstract method
        return self.length * self.width

    def perimeter(self):  # Implementing the abstract method
        return 2 * (self.length + self.width)

# shape = Shape()  # ❌ This will raise an error! Cannot instantiate an abstract class

circle = Circle(5)  # ✅ Works fine because Circle implements all abstract methods
rectangle = Rectangle(4, 6)  # ✅ Works fine

print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Rectangle Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")


'''
How @abstractmethod Works
Shape is an abstract class with two abstract methods: area() and perimeter().

We must implement both methods in Circle and Rectangle because they inherit from Shape.

If we don’t implement the abstract methods in a subclass, Python will raise an error when trying to create an instance of that subclass.

We cannot create an object of Shape directly because it contains abstract methods.
'''