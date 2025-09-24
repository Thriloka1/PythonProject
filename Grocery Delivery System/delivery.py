from collections import defaultdict, deque
import heapq
from geopy.geocoders import Nominatim

class DeliveryGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_route(self, u, v, distance):
        self.graph[u].append((v, distance))
        self.graph[v].append((u, distance))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            curr_dist, node = heapq.heappop(pq)
            if curr_dist > distances[node]:
                continue
            for neighbor, weight in self.graph[node]:
                d = curr_dist + weight
                if d < distances[neighbor]:
                    distances[neighbor] = d
                    heapq.heappush(pq, (d, neighbor))
        return distances

# Geopy setup
geolocator = Nominatim(user_agent="grocery_delivery_system")
warehouse_address = "Andhra Pradesh, India"
warehouse_location = geolocator.geocode(warehouse_address)
warehouse_coords = (warehouse_location.latitude, warehouse_location.longitude)

# Create the delivery map instance
delivery_map = DeliveryGraph()
