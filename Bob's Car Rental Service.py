class showRoom:
    def __init__(self, brand, year, rental_ppd):
        self.brand = brand
        self.year = year
        self.rental_ppd = rental_ppd
def display_info():
    brand = input("Enter the car brand: ")
    year = input("Enter the year: ")
    rental_ppd = input("Enter the Rental per day: ")
    print(f"Car: {brand}, Year: {year}, Rental price: ${rental_ppd}/day")

display_info()