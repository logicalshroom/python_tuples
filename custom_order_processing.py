#  Task 3: Customer Order Processing

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

def prntorders(order_list):
    for order in order_list:
        print (f"{order[0]} ordered {order[2]} of the item {order[1]}")

prntorders(orders)