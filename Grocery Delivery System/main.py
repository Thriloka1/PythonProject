from inventory import generate_inventory,show_inventory,add_inventory_item
from auth import register_user,login,logout,add_admin
from search import linear_search
from orders import place_order,view_my_orders,view_all_orders
from customers import customers
from simulation import process_orders_simulation,simulate_multiple_users
from delivery import delivery_map



def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. View Inventory")
        print("2. Add Inventory Item")
        print("3. View Customers")
        print("4. View All Orders")
        print("5. Process Orders")
        print("6. Add New Admin")
        print("7. Simulate Multiple Users")
        print("8. Logout")
        choice = input("Enter choice: ")
        if choice == "1": show_inventory()
        elif choice == "2": add_inventory_item()
        elif choice == "3": customers.display_customers()
        elif choice == "4": view_all_orders()
        elif choice == "5": process_orders_simulation(delivery_map)
        elif choice == "6": add_admin()
        elif choice == "7": simulate_multiple_users()
        elif choice == "8": logout(); break
        else: print("Invalid choice.")


def user_menu(user):
    while True:
        print("\n=== User Menu ===")
        # print("1. View Inventory")
        print("1. Search Item")
        print("2. Place Order")
        print("3. View My Orders")
        print("4. Logout")
        choice = input("Enter choice: ")
        if choice == "1": linear_search()
        elif choice == "2": place_order(user)
        elif choice == "3": view_my_orders(user)
        elif choice == "4": logout(); break
        else: print(" Invalid choice.")


def main():
    generate_inventory()
    while True:
        print("\n Grocery Delivery system")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
        choice=input("Enter choice: ")
        if choice=='1': register_user()
        elif choice =='2':
            user=login(delivery_map)
            if user['role']=='admin':admin_menu()
            else: user_menu(user)


if __name__ == "__main__":
    main()
