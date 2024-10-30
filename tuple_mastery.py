# Task 1: Fromatting Flight Itineraries

# 1. Initialize function and Accept Multiple Tuple Inputs
# 2. Slice each Tuple
# 3. Print output String

def flightform(itinerary):
    counter = 1
    for i in itinerary:
        print(f"Itinerary {counter}: {i[0]} - From {i[1]} to {i[2]}")
        counter += 1

# initilize the list for passing into the function

flightlist = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

flightform(flightlist)