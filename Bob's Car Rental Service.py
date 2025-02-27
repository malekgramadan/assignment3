class showRoom:
    def __init__(self, brand, model, year, rental_ppd):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_ppd = rental_ppd
def display_info():
    brand = input("Enter the car brand: ")
    model = input("Enter the car's model: ")
    year = input("Enter the year: ")
    rental_ppd = input("Enter the Rental per day: ")
    brd = showRoom(brand)
    print(f"Car: {brd} {model}, Year: {year}, Rental price: ${rental_ppd}/day")

display_info()