from collections import deque

from inventory import is_item_available, show_inventory
from customers import customers


order_queue=deque()
all_orders=[]
user_orders={}
def place_order(user):
    show_inventory()
    cart=[]
    customer_name = user['username']

    # Retrieve the CustomerNode
    customer_node = customers.get_customer_by_name(customer_name)
    while True:
        if not cart:
            print(" No valid items to order.")
        while True:
            item_name=input("search products")
            if is_item_available(item_name):
                cart.append(item_name)
            else:
                print(f" {item_name}' is out of stock. Removed from cart.")
            proceed = input("Do you want to add more items? (yes/no): ").strip().lower()
            if proceed == "no":
                break
        break
    if cart:
        for item_name in cart:
            order_id = len(all_orders) + 1
            order = {
                "order_id": order_id,
                "item": item_name,
                "customer": customer_node.name,  # use CustomerNode
                "location": customer_node.location
            }
            order_queue.append(order)
            all_orders.append(order)
            user_orders.setdefault(customer_node.name, []).append(order)
            print(f" Order {order_id} placed: {item_name} -> {order['location']}")
        
def view_all_orders():
    if not  all_orders:
        print("no orders yet")
        return
    print(" All orders")
    for o in all_orders:
        print(f"{o['order_id']}:{o['item']} for {o['customer']} at {o['location']}")



def view_my_orders(user):

    show_inventory()
    orders= user_orders.get(user['username'],[])
    if not orders:
        print("no orders placed yet")
        return
    for o in orders:
        print(f"{o['order_id']}:{o['item']} to {o['location']}")
