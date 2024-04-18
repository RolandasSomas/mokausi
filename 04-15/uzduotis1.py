"""
Parašykite klasę CoffeeShop, kuri turi tris inicializuotos klasės kintamuosius:
name: str (iš esmės parduotuvės pavadinimas)
meniu : elementų sąrašas (list) (dict tipo), kuriame kiekvienas elementas turi elementą (elemento pavadinimą), tipą (ar tai maistas, ar gėrimas) ir kainą.
orders: tuščias list
ir septyni metodai:
add_order: į užsakymų sąrašo pabaigą įtraukia prekės pavadinimą, jei jis yra meniu, priešingu atveju grąžina "Šiuo metu šios prekės nėra!".
fulfill_order: jei užsakymų sąrašas nėra tuščias, grąžinama "{prekė} yra paruošta!". Jei užsakymų sąrašas tuščias, grąžinkite "Visi užsakymai įvykdyti!".
list_orders: grąžina priimtų užsakymų prekių pavadinimus, priešingu atveju - tuščią sąrašą.
due_amount: grąžina bendrą mokėtiną sumą už priimtus užsakymus.
cheapest_item: grąžina pigiausio meniu elemento pavadinimą.
drinks_only: grąžina tik meniu gėrimų tipo elementų pavadinimus.
food_only: grąžina tik meniu maisto tipo elementų pavadinimus.
"""


class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item):
        for element in self.menu:
            if element["name"] == item:
                self.orders.append(item)
                return
        return "Sorry we dont have this product now!"

    def fulfill_order(self):
        if self.orders:
            item = self.orders.pop(0)
            return f"{item} is prepared!"
        else:
            return "All order is execute!"

    def list_orders(self):
        return self.orders

    def due_amount(self):
        total = 0
        for item in self.orders:
            for element in self.menu:
                if element["name"] == item:
                    total += element["price"]
        return total

    def cheapest_item(self):
        cheapest = min(self.menu, key=lambda x: x["price"])
        return cheapest["name"]

    def drinks_only(self):
        drinks = [
            element["name"] for element in self.menu if element["type"] == "drink"
        ]
        return drinks

    def food_only(self):
        food = [element["name"] for element in self.menu if element["type"] == "food"]
        return food


menu = menu = [
    {"name": "Margherita Pizza", "type": "food", "price": 8.50},
    {"name": "Pepperoni Pizza", "type": "food", "price": 9.50},
    {"name": "Caesar Salad", "type": "food", "price": 7.00},
    {"name": "Carbonara Pasta", "type": "food", "price": 8.00},
    {"name": "Espresso", "type": "drink", "price": 2.00},
    {"name": "Cappuccino", "type": "drink", "price": 2.50},
    {"name": "Mineral Water", "type": "drink", "price": 1.50},
    {"name": "Orange Juice", "type": "drink", "price": 3.00}
]
coffee_shop = CoffeeShop("MyCoffeeShop", menu)
# print(coffee_shop.add_order("Coffee"))
# print(coffee_shop.add_order("Juice"))
print(coffee_shop.fulfill_order())
print(coffee_shop.list_orders())
print(coffee_shop.due_amount())
print(coffee_shop.cheapest_item())
print(coffee_shop.drinks_only())
print(coffee_shop.food_only())
