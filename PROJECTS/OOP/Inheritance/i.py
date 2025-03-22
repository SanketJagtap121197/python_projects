# Base class Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        """Constructor to initialize vehicle attributes."""
        self.brand = brand  # Store the brand of the vehicle
        self.model = model  # Store the model of the vehicle
        self.year = year    # Store the manufacturing year of the vehicle

    def display_info(self):
        """Method to display vehicle details."""
        print(f"\nVehicle Information:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}")

# Derived class Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        """Constructor to initialize Car attributes, including inherited attributes."""
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.fuel_type = fuel_type  # Store the fuel type of the car

    def display_info(self):
        """Method to display car details including fuel type."""
        super().display_info()  # Call the display_info method from Vehicle
        print(f"Fuel Type: {self.fuel_type}")

# Derived class Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        """Constructor to initialize Bike attributes, including inherited attributes."""
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.engine_capacity = engine_capacity  # Store the engine capacity of the bike

    def display_info(self):
        """Method to display bike details including engine capacity."""
        super().display_info()  # Call the display_info method from Vehicle
        print(f"Engine Capacity: {self.engine_capacity} cc")

# Taking user input to create Car object
print("Enter details for the Car:")
car_brand = input("Enter car brand: ")  # User inputs car brand
car_model = input("Enter car model: ")  # User inputs car model
car_year = input("Enter car year: ")    # User inputs car manufacturing year
car_fuel = input("Enter fuel type (Petrol/Diesel/Electric): ")  # User inputs fuel type

# Creating a Car object
car = Car(car_brand, car_model, car_year, car_fuel)

# Taking user input to create Bike object
print("\nEnter details for the Bike:")
bike_brand = input("Enter bike brand: ")  # User inputs bike brand
bike_model = input("Enter bike model: ")  # User inputs bike model
bike_year = input("Enter bike year: ")    # User inputs bike manufacturing year
bike_engine = input("Enter engine capacity (in cc): ")  # User inputs engine capacity

# Creating a Bike object
bike = Bike(bike_brand, bike_model, bike_year, bike_engine)

# Display details of Car and Bike
print("\nCar Details:")
car.display_info()

print("\nBike Details:")
bike.display_info()
