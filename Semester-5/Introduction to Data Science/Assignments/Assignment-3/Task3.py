#Part A
class DivisionByZeroError(Exception):
    def __init__(self, message="Cannot divide by zero"):
        super().__init__(message)

def divide_by(numbers, divisor):
    try:
        if divisor == 0:
            raise DivisionByZeroError()
        results = [num / divisor for num in numbers]
    except TypeError as te:
        raise DivisionByZeroError(f"Division by zero error occurred due to non-numeric input: {te}")
    except ValueError as ve:
        raise DivisionByZeroError(f"Division by zero error occurred due to division error: {ve}")
    return results

numbers = [1, 2, 3, 4]
divisor = 2

try:
    results = divide_by(numbers, divisor)
    print(results)
except DivisionByZeroError as e:
    print(f"Error: {e}")

#Part B
def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred in {func.__name__}:")
            print(f"Type: {type(e).__name__}")
            print(f"Message: {str(e)}")
            traceback.print_exc()

    return wrapper

@log_exceptions
def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Division by zero!")