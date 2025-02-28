class Vechile:
    def __init__(self, brand, model, year, rental_ppd):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_ppd = rental_ppd

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Rental price: ${self.rental_ppd}/day")

brand = input("Enter the car brand: ")
model = input("Enter the car's model: ")
year = input("Enter the year: ")
rental_ppd = input("Enter the Rental per day: ")
car = Vechile(brand, model, year, rental_ppd)
car.display_info()