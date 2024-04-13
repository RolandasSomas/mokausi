class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name:str, price=float, quantity=0):
        assert price >= 0, f'Price {price} is not greater or equal than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

Item1 = Item('Phone', 100, 2)
Item2 = Item('Laptop', 1000, 3)
Item3 = Item('Cable', 10, 5)
Item4 = Item('Mouse',50, 5)
Item5 = Item('Keyboard',75, 5)


# print(Item1.name,Item1.price, Item1.quantity)
# print(Item2.name, Item2.price, Item2.quantity)
#
# print(Item1.calculate_total_price())
#
# print(Item2.__dict__)
# Item1.apply_discount()
# print(Item1.price)
# Item2.pay_rate=0.7
# Item2.apply_discount()
# print(Item2.price)
print(Item.all)

for instance in Item.all:
    print(instance.name)