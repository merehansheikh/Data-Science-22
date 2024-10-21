# Task 05: Input a three-digit number and reverse the number by separating digits
x=int(input('Enter three-digit number:'))
hundreds=x//100
tens=(x%100)//10
units=(x%100)%10
print (f'Reverse number is: {units}{tens}{hundreds}')
