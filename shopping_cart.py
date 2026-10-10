# Raw stock delivery data
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
]

# Customer shopping cart (List of products they want to buy)
shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]

def build_inventary(delivery):
    inventory = {}
    for name,price,qty in delivery:
        if name in inventory:
            inventory[name]['quantity'] += qty
        else:
            inventory[name] = {'price': price, 'quantity': qty}

    return inventory

inventory = build_inventary(raw_delivery)

