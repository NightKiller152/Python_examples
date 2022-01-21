import random


class Fighter:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, enemy):
        if enemy.hp > self.atk:
            enemy.hp = enemy.hp - self.atk
        else:
            enemy.hp = 0


cat = Fighter('Bobo', 100, 14)
dog = Fighter('Dage', 88, 23)

Dattacks = random.randint(1, 10)
Cattacks = random.randint(1, 10)

while Dattacks > 0:
    dog.attack(cat)
    print(f"cat hp: {cat.hp},  dog hp: {dog.hp}")
    Dattacks -= 1

while Cattacks > 0:
    cat.attack(dog)
    print(f"cat hp: {cat.hp},  dog hp: {dog.hp}")
    Cattacks -= 1

print(f"cat hp: {cat.hp},  dog hp: {dog.hp}")