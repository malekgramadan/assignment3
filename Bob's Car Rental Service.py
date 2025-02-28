class Vehicle:
    def __init__(self, brand, model, year, rental_ppd,seat_capacity,engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_ppd = rental_ppd
        self.seat_capacity = seat_capacity
        self.engine = engine

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year},Seats: {self.seat_capacity}, Rental price: ${self.rental_ppd}/day")
        print(f"Bike: {self.brand} {self.model}, Year: {self.year},Engine: {self.engine}, Rental price: ${self.rental_ppd}/day")

    def calculate_rental_cost(self, days):
        return print(f"Rental cost for the {self.brand} {self.model} for {days} days: ${int(self.rental_ppd * days)}")
    
brand = input("Enter the car brand: ")
model = input("Enter the car's model: ")
year = input("Enter the year: ")
rental_ppd = input("Enter the Rental per day: ")
seat_capacity = input("Enter the seat capacity: ")
days = int(input("Enter the number of days you want to rent the car: "))
engine = input("Enter the engine type: ")
car = Vehicle(brand, model, int(year), int(rental_ppd), int(seat_capacity), engine)
car.display_info()
car.calculate_rental_cost(days)