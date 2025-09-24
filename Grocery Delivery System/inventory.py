import random
import string

inventory=[]

def generate_inventory(size=10000):
    for i in range(size):
        name=''.join(random.choices(string.ascii_uppercase, k=5))
        price=round(random.uniform(1,100),2)
        inventory.append({"id":100+i,"name":name,"price":price})

def show_inventory():
    for item in inventory:
        print(f"{item['name']} - ${item['price']}")


def is_item_available(item_name):
    return any(item["name"].lower() == item_name.lower() for item in inventory)


def add_inventory_item():
    name=input("enter item name")
    price=float(input("enter price"))
    inventory.append({"name":name,"price":price})
    print("Added!...")

