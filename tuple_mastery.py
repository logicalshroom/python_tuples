# Task 1: Fromatting Flight Itineraries

# 1. Initialize function, ticket number counter
# 2. Iterate over each item in the outer list
# 3. Print a string with the required Tuple items
# 4. Tick up the ticket number counter

def flightform(itinerary):
    counter = 1
    for i in itinerary:
        print(f"Itinerary {counter}: {i[0]} - From {i[1]} to {i[2]}")
        counter += 1

# initilize the list for passing into the function

flightlist = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

flightform(flightlist)