from random import*
def print_random_numbers(n,a,b):
    for i in range (n):
        print (randint(a,b),end=' ')
print_random_numbers(5,10,50)
