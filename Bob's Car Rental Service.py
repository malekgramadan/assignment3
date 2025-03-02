class Vehicle:
    def __init__(self, brand, model, year, rental_ppd):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_ppd = rental_ppd

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nRental Price Per Day: ${self.__rental_ppd}/day")

    def calculate_rental_cost(self, days):
        return self.__rental_ppd * days
    
    def get_rental_ppd(self):
        return self.__rental_ppd
    
    def set_rental_ppd(self, price):
        if price > 0:
            self.__rental_ppd = price
        else:
            print("Error: Price must be greater than 0.")

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_ppd, seats):
        super().__init__(brand, model, year, rental_ppd)
        self.seats = seats
    
    def display_info(self):
        print(f"Brand: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seats}, Rental Price Per Day: ${self.get_rental_ppd()}/day")

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_ppd, engine):
        super().__init__(brand, model, year, rental_ppd)
        self.engine = engine
    
    def display_info(self):
        print(f"Brand: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine}cc, Rental Price Per Day: ${self.get_rental_ppd()}/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()

vehicles = []
action = 0
print("Bob's Car Rental Service")
while action != 5:
    print("1. Add a Car")
    print("2. Add a Bike")
    print("3. Calculate Rental Cost")
    print("4. Set Rental Price")
    print("5. Exit")
    print("=====================================")
    action = int(input("Enter your choice: "))
    
    if action == 1:
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        rental_price = float(input("Rental Price per Day: "))
        seats = int(input("Seating Capacity: "))
        car = Car(brand, model, year, rental_price, seats)
        vehicles.append(car)
        print("Car details have been added.")
        print(" ")
    elif action == 2:
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        rental_price = float(input("Rental Price per Day: "))
        engine = int(input("Engine Capacity: "))
        bike = Bike(brand, model, year, rental_price, engine)
        vehicles.append(bike)
        print("Bike details have been added.")
        print(" ")
    elif action == 3:
        if vehicles:
            days = int(input("Enter the number of days to calculate rental costs: "))
            print(" ")
            print("Rental Costs:")
            print(" ")
            for vehicle in vehicles:
                print(f"Rental cost for {vehicle.brand} {vehicle.model} for {days} days: ${vehicle.calculate_rental_cost(days)}")
                print(" ")
        else:
            print("No vehicles available to calculate rental costs.")
            print(" ")
    elif action == 4:
        if vehicles:
            for vehicle in vehicles:
                new_price = float(input(f"Enter new rental price for {vehicle.brand} {vehicle.model}: "))
                vehicle.set_rental_ppd(new_price)
            print("Rental price has been updated.")
            print(" ")
        else:
            print("No vehicles available to update rental prices.")
            print(" ")
    elif action == 5:
        print("Exiting Bob's Car Rental Service")
        print(" ")
    else:
        print("Invalid choice. Please try again.")
