'''
Using Private Variables
In Python, encapsulation is implemented using private variables (denoted by __ before a variable name).
'''

class Car:
    def __init__(self, brand, speed):
        self.brand = brand            # Public variable (accessible directly)
        self.__speed = speed          # Private variable (encapsulated)

    def accelerate(self, increase):
        """Increase the speed if the value is positive."""
        if increase > 0:
            self.__speed += increase
            print(f"New speed: {self.__speed} km/h")
        else:
            print("Invalid speed increment")

    def get_speed(self):
        """Getter method to access private speed."""
        return self.__speed

    def set_speed(self, speed):
        """Setter method to safely update speed."""
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative!")

# Usage
car = Car("Tesla", 50)
car.accelerate(20)       # Allowed: Changes speed
print(car.get_speed())   # Allowed: Accesses private data via getter

# car.__speed = 100       # Not allowed: Direct modification (Name mangling)

'''
How Encapsulation Works Internally
__speed is a private variable, so it cannot be accessed directly (car.__speed will cause an error).

Instead, we access and modify the variable using getter (get_speed) and setter (set_speed) methods.

Python internally renames private variables (name mangling) to _ClassName__variable to prevent direct access.

For example, __speed becomes _Car__speed. This is why car.__speed doesn’t work.

However, you can still access the private variable using the modified name (e.g., car._Car__speed).

This is discouraged because it breaks the encapsulation principle.

Encapsulation is a way to protect data from accidental modification and enforce controlled access via methods.

In the Car class, the speed attribute is private, and we use getter and setter methods to access and modify it.

This way, we can ensure that the speed is always positive and prevent invalid speed increments.

Encapsulation is a fundamental concept in object-oriented programming that helps in maintaining code quality and security.'''

'''
Advantages of Encapsulation
✅ Protects Data: Prevents accidental modification of critical variables.
✅ Better Control: Provides controlled access to attributes via getters and setters.
✅ Encourages Maintainability: Ensures that code changes don’t break other parts of the program.
✅ Security: Sensitive information (e.g., passwords, bank balances) remains hidden.
'''