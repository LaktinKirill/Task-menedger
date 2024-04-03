from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self):
        return "Игрок наносит удар мечом"
class Bow(Weapon):
    def attack(self):
        return "Игрок стреляет из лука"
class Axe(Weapon):
    def attack(self):
        return "Боец наносит мощный удар топором."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None
    def changeWeapon(self, weapon):
        self.weapon = weapon
    def fight(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return f"{self.name} не может атаковать без оружия!"
class Monster:
    def __init__(self, name):
        self.name = name
def fightScene(fighter, monster):
    print(f"Боец {fighter.name} выбирает {type(fighter.weapon)}")
    print(fighter.fight())
    print(f"{monster.name} побежден!\n")
fighter = Fighter("Герой")
monster = Monster("Огр")

fighter.changeWeapon(Sword())
fightScene(fighter, monster)

