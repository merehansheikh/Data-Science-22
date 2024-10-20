#Part A
def filter_invalid(orders):
    def is_valid(order):
        try:
            total = float(order['total'])
            return total > 0
        except ValueError:
            return False

    return list(filter(is_valid, orders))

# Example usage
orders = [
    {"customer": "Alice", "total": 250.5}, 
    {"customer": "Bob", "total": "invalid_data"}, 
    {"customer": "Charlie", "total": 450}, 
    {"customer": "Daisy", "total": 100.0}, 
    {"customer": "Eve", "total": -30},  # Invalid total 
]

valid_orders = filter_invalid(orders)
print(valid_orders)