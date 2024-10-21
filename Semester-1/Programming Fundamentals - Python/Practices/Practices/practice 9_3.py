# Task 03: Input a three-digit number and print it's digits in single line using integer division and remainder
x=int(input('Enter three-digit number:'))
hundreds=x//100
tens=(x%100)//10
units=(x%100)%10
print (f'First digit: {hundreds}')
print (f'Second Digit: {tens}')
print (f'Third digit: {units}')
