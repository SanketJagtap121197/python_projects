# Parent class
class Animal:
    def __init__(self, name):  # Constructor to initialize the name
        self.name = name  # Assigning name to the instance variable
    
    def make_sound(self):  # Method to make a sound
        return "Some generic sound"  # Default sound for an animal

# Child class inheriting from Animal
class Dog(Animal):
    def make_sound(self):  # Overriding the parent class method
        return "Bark"  # Specific sound for a dog

# Child class inheriting from Animal
class Cat(Animal):
    def make_sound(self):  # Overriding the parent class method
        return "Meow"  # Specific sound for a cat

# Taking user input
animal_name = input("Enter a general animal name: ")
dog_name = input("Enter a dog name: ")
cat_name = input("Enter a cat name: ")

# Creating objects
animal = Animal(animal_name)
dog = Dog(dog_name)
cat = Cat(cat_name)

# Displaying results
print(f"{animal.name} makes sound: {animal.make_sound()}")  # Calls method from Animal class
print(f"{dog.name} makes sound: {dog.make_sound()}")  # Calls overridden method from Dog class
print(f"{cat.name} makes sound: {cat.make_sound()}")  # Calls overridden method from Cat class
