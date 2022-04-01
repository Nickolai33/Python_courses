# создание класса Car
class Car:

    # создание методов класса
    def __str__(self):
        return "Car class Object"

    def start(self):
        print("Двигатель заведен")

car_a = Car()
print(car_a)