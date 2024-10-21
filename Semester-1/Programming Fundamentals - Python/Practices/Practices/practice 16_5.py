# 5. Input an integer. Run a loop from 2 to the integer, check and print numbers 
# completely divides the input integer.

x=int(input('Number: '))
i=2
while i<=x:
    if x%i==0:
        print (f'{x} is completely divisible by {i}')
    i=i+1
