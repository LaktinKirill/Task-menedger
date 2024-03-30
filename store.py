class Store():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.itims = {}
    def add_product(self, name_product, price):
        self.itims[name_product] = price
        print(f"Товар {name_product} был добавлен в ассортимент магазина {self.name}")

    def delete_product(self, name_product):
        if name_product in self.itims:
            del self.itims[name_product]
            print(f"Товар {name_product} был удален из ассортимента магазина {self.name}")

    def get_price(self, name_product):
        if name_product in self.itims:
            return self.itims.get(name_product)
        else:
            print("None")

    def new_price(self, name_product, price2):
        if name_product in self.itims:
            self.itims[name_product] = price2
            print(f"Стоимость товара {name_product} обновлена в магазине {self.name}")
        else:
            print("Товар не найден")

store1 = Store("Оазис", "Мира 24")
store2 = Store("Илона", "Маклина 46")
store3 = Store("Краное Белое", "Октябрьский 98")

store1.add_product("Хлеб", "24.50")
store1.add_product("Колбаса", "318.50")
store1.add_product("Яблоки", "99.99")
store1.add_product("Пиво", "55.50")

store1.delete_product("Колбаса")
print(store1.get_price("Яблоки"))
store1.new_price("Пиво", 45.90)

