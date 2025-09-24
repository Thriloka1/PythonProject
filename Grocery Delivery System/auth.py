from geopy import Nominatim
from geopy.distance import geodesic

from customers import customers
geolocator = Nominatim(user_agent="grocery_delivery_system")
warehouse_address = "Andhra Pradesh, India"
warehouse_location = geolocator.geocode(warehouse_address)
warehouse_coords = (warehouse_location.latitude, warehouse_location.longitude)

users_db= {"Sherlock":
               {"password":"Holmes","role":"admin"}
            }

current_user=None

def register_user():
    username=input("\n enter username")
    if username in users_db:
        print("\n user already exists")
        return
    password=input("\n enter password")
    users_db[username]={"password":password,"role":"user"}
    print(f"user {username} registered successfully")

def login(delivery_map):
    global current_user
    username=input("\n username")
    password=input("\n password")
    user=users_db.get(username)
    if not user or user['password']!=password:
        print("invalid credentials")
        return None
    current_user={'username':username,'role':user['role']}
    print("login successful")

    if user['role'] == 'user':
        if not customers.get_customer_by_name(username):
            # Force user to enter a valid location
            while True:
                user_address = input("\nEnter your location (required): ")
                user_location = geolocator.geocode(user_address)
                if user_location:
                    break
                print(" Could not find the location. Please enter a valid location.")

            customers.add_customer(username, user_address)
            user_coords = (user_location.latitude, user_location.longitude)
            distance_km = geodesic(warehouse_coords, user_coords).km
            print(f"Distance from warehouse to {user_address}: {distance_km:.2f} km")

            # Add dynamic route to delivery_map
            delivery_map.add_route("Warehouse", user_address, distance_km)
            print(f"Added delivery route: Warehouse -> {user_address} ({distance_km:.2f} km)")
    return current_user

def add_admin():
    if current_user["role"] != "admin":
        print(" Only admins can add new admins.")
        return
    username = input("New admin username: ")
    if username in users_db:
        print(" Already exists.")
        return
    password = input("New admin password: ")
    users_db[username] = {"password": password, "role": "admin"}
    print(f" Admin added successfully!...")

def logout():
    global current_user
    if current_user:
        current_user=None




