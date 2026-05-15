class Restaraunt:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}, Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт")

Restaurant1 = Restaraunt("5 углов", "Итальянская")
Restaurant2 = Restaraunt("Азия", "Азиатская")
Restaurant3 = Restaraunt("Борщец", "Русская")



Restaurant1.describe_restaurant()
Restaurant2.describe_restaurant()
Restaurant3.describe_restaurant()