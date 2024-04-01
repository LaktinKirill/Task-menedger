class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass
class Bird(Animal):
    def __init__(self, food, name, age):
        super().__init__(name, age)
        self.food = food
    def eat(self):
        print(f"{self.name}, ест {self.food}")
    def make_sound(self):
        print("Кря-кря")
class Mammal(Animal):
    def __init__(self, food, name, age):
        super().__init__(name, age)
        self.food = food
    def eat(self):
        print(f"{self.name}, ест {self.food}")
    def make_sound(self):
        print("Рррррррррр")
class Reptile(Animal):
    def __init__(self, food, name, age):
        super().__init__(name, age)
        self.food = food
    def eat(self):
        print(f"{self.name}, ест {self.food}")
    def make_sound(self):
        print("Гррррррррр")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
def eat_food(animals):
    for animal in animals:
        animal.eat()
animals = [Bird( "Семечки", "Кукушка", 2), Mammal("Мясо", "Собака", 4), Reptile("Рыба", "Крокодил", 3)]

animal_sound(animals)
eat_food(animals)


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

