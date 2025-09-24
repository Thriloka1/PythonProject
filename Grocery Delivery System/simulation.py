import random
import threading
import time

from customers import customers
from inventory import inventory
from orders import all_orders,order_queue,user_orders

def user_place_orders(username):
    customer = customers.get_customer_by_name(username)
    if not customer:
        return

    available_items = [item['name'] for item in inventory]

    for item_name in available_items:  # No num_orders, loop through all items
        order_id = len(all_orders) + 1
        order = {
            "order_id": order_id,
            "item": item_name,
            "customer": customer.name,
            "location": customer.location
        }
        order_queue.append(order)
        all_orders.append(order)
        user_orders.setdefault(username, []).append(order)
        print(f"[{username}] Placed order {order_id}: {item_name} -> {customer.location}")
        time.sleep(random.uniform(0.1, 0.5))  # small delay to simulate real ordering


def process_orders_simulation(delivery_map):
    if not order_queue:
        print("No pending orders.")
        return
    print("\nProcessing Orders:")
    while order_queue:
        order = order_queue.popleft()
        loc = order['location']

        distance_map = delivery_map.dijkstra("Warehouse")
        distance = distance_map.get(loc, float('inf'))

        if distance == float('inf'):
            print(f" Cannot calculate path to {loc}. Skipping delivery.")
            continue
        print(f"Order {order['order_id']}: {order['item']} for {order['customer']} at {loc}")
        print(f"Shortest path distance: {distance} km")
        print(f" your order(s) will be delivered soon!\n")

def simulate_multiple_users():
    threads = []
    from auth import users_db
    for username, user in users_db.items():
        if user['role'] == 'user':
            t = threading.Thread(target=user_place_orders, args=(username,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()
    print("\n All users placed orders for all available items.")
