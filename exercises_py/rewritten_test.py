###REWRITTEN CODE###


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell_product(self, amount):
        self.quantity -= amount

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'


class Inventory:

    products: list[Product] = []

    @classmethod
    def add_product(cls, product: Product):
        cls.products.append(product)

    def __str__(self):
        return '\n'.join(str(product) for product in self.products)


def main():
    inventory = Inventory()
    Inventory.add_product(Product('Apple', 1.0, 10))
    Inventory.add_product(Product('Banana', 0.5, 15))
    Inventory.add_product(Product('Orange', 1.5, 8))
    print(f'\tInitial inventory:\n{inventory}')

    inventory.products[0].sell_product(5)
    print(f'\tUpdated inventory:\n{inventory}')


if __name__ == '__main__':
    main()
