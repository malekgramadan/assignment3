class Vechile:
    def __init__(self, brand, model, year, rental_ppd):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_ppd = rental_ppd

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Rental price: ${self.rental_ppd}/day")

    def calculate_rental_cost(self, days):
        return print(f"Rental cost for {self.brand} {self.model} {int(self.rental_ppd * days)}")
    
brand = input("Enter the car brand: ")
model = input("Enter the car's model: ")
year = input("Enter the year: ")
rental_ppd = input("Enter the Rental per day: ")
days = int(input("Enter the number of days you want to rent the car: "))
car = Vechile(brand, model, year, rental_ppd)
car.display_info()
car.calculate_rental_cost(days)