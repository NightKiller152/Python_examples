class Animal():
    def __init__(self, name, weight, color, sex):
        self.__name = name
        self.__weight = weight
        self.__color = color
        self.__sex = sex
    def get_animal(self):
        print(f'Name: {self.__name}, Color: {self.__color}, Sex: {self.__sex}, Weight: {self.__weight}, Legs: {self.legs}')


class Horse(Animal):
    legs = 'Hard'


class Dog(Animal):
    legs = 'Soft'


class Cat(Animal):
    legs = 'Furry'


horse = Horse('Bolt', 250, 'Brown', 'Male')
dog = Dog('Breety', 25, 'Black', 'Female')
cat = Cat('Rich', 6, 'Multicolor', 'Male')

print(horse.get_animal(), dog.get_animal(), cat.get_animal())