import time
from inventory import inventory, show_inventory


def linear_search():
    show_inventory()
    name=input("enter name")
    start=time.time()

    found_item=None

    for item in inventory:
        if item['name'].lower()==name.lower():
            found_item=item
            break
    end=time.time()

    if found_item:
        print(f" found {found_item['name']} - {found_item['price']}")
    else:
        print("not found")
    print(f"⏱ Search took {(end - start) * 1000:.4f} ms")