# Task 02: Input decimal number and print octal number in reverse order.
x=int(input('Decimal number: '))
y=()
while x!=0:
    y=x%8
    print (y,end='')
    x=x//8
