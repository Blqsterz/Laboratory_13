class Restaraunt:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}, Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт")
    
    def change_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана: {new_rating}")

newRestaurant = Restaraunt("5 углов", "Итальянская")
new_rating=int(input("Введите рейтинг ресторана:"))

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
newRestaurant.change_rating(new_rating)