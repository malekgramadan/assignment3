class Vehicle:
    def __init__(self, brand, model, year, rental_ppd):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_ppd = rental_ppd

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nRental Price Per Day: ${self.__rental_ppd}/day")

    def calculate_rental_cost(self, days):
        return print(f"Rental cost for the {self.brand} {self.model} for {days} days: ${int(self.rental_ppd * days)}")

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_ppd, seats):
        super().__init__(brand, model, year, rental_ppd)
        self.seats = seats
    
    def display_info(self):
        print(f"Brand: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seats}, Rental Price Per Day: ${self._Vehicle__rental_ppd}/day")

car =[Car("Toyota", "Corolla", 2015, 50, 5)]
car[0].display_info()