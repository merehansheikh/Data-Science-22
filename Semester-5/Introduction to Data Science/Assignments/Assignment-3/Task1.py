from functools import reduce

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

#Part B
def apply_discount(orders):
    return list(map(lambda order: {**order, 'total': order['total'] * 0.9 if order['total'] > 300 else order['total']}, orders))

discounted = apply_discount(valid_orders)
print(discounted)

#Part C
def total_sales(orders):
    return reduce(lambda total, order: total + order['total'], orders, 0)

total = total_sales(discounted)
print(total)