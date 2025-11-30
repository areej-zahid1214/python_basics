class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    def item_total(self):
        return self.product.price * self.quantity
p1 = Product("Soap", 100)
p2 = Product("Shampoo", 250)
p3 = Product("Oil", 300)
item1 = CartItem(p1, 2)  
item2 = CartItem(p2, 1)  
item3 = CartItem(p3, 3)   
total_bill = item1.item_total() + item2.item_total() + item3.item_total()
print("Total Bill =", total_bill)
