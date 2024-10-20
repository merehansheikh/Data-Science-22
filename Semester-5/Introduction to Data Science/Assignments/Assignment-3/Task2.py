#Part A
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            result = self.i ** 2
            self.i += 1
            return result
        else:
            raise StopIteration
        
for square in SquareIterator(5):
    print(square)

#Part B
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for fib in fibonacci_generator(10):
    print(fib)