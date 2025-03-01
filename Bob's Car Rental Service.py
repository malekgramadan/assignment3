class Vehicle:
    def __init__(self, brand, model, year, rental_ppd):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_ppd = rental_ppd

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nRental Price Per Day: ${self.__rental_ppd}/day")

    def calculate_rental_cost(self, days):
        return print(f"Rental cost for the {self.brand} {self.model} for {days} days: ${int(self.__rental_ppd * days)}")
    
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

# car =[Car("Toyota", "Corolla", 2015, 50, 5)]
# bike = [Bike("Yamaha", "R1", 2019, 30, 998)]
# car[0].display_info()
# bike[0].display_info()
# car[0].calculate_rental_cost(3)
# bike[0].calculate_rental_cost(4)
# car[0].set_rental_ppd(60)
# bike[0].set_rental_ppd(40)
# car[0].display_info()
# bike[0].display_info()

car =[]
bike = []
action = 0

while action != 5:
    print("1. Add a Car")
    print("2. Add a Bike")
    print("3. Calculate Rental Cost")
    print("4. Set Rental Price")
    print("5. Exit")
    action = int(input("Enter your choice: "))