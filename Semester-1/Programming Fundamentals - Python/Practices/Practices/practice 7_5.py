# Task 05: Input a number, check and print messages (see sample runs carefully for understanding):
# Sample Runs:
# Number: 16
# Number is divisible by 2 only
# Number: 9
# Number is divisible by 3 only
# Number: 18
# Number is divisible by both by 2 and 3
# Number: 15
# Number is divisible by by both 5 and 3
# Number: 63
# Number is divisible by by both 3 and 7
# Check for 2, 3, 5, and 7.

x=int(input('Numbrt:'))
divide1=x%2
divide2=x%3
divide3=x%5
divide4=x%7
if divide1==0 and divide2!=0 and divide3!=0 and divide4!=0:
    print (f'Number is divisible by 2 only')
elif divide1!=0 and divide2==0 and divide3!=0 and divide4!=0:
    print (f'Number is divisible by 3 only')
elif divide1!=0 and divide2!=0 and divide3==0 and divide4!=0:
    print (f'Number is divisible by 5 only')
elif divide1!=0 and divide2==0 and divide3!=0 and divide4==0:
    print (f'Number is divisible by 7 only')
elif divide1==0 and divide2==0 and divide3!=0 and divide4!=0:
    print (f'Number is divisible by 2 and 3 only')
elif divide1==0 and divide2!=0 and divide3==0 and divide4!=0:
    print (f'Number is divisible by 2 and 5 only')
elif divide1==0 and divide2!=0 and divide3!=0 and divide4==0:
    print (f'Number is divisible by 2 and 7 only')
elif divide1!=0 and divide2==0 and divide3==0 and divide4!=0:
    print (f'Number is divisible by 3 and 5 only')
elif divide1!=0 and divide2==0 and divide3!=0 and divide4==0:
    print (f'Number is divisible by 3 and 7 only')
elif divide1!=0 and divide2!=0 and divide3==0 and divide4==0:
    print (f'Number is divisible by 5 and 7 only')
elif divide1==0 and divide2==0 and divide3==0 and divide4!=0:
    print (f'Number is divisible by 2,3 and 5 only')
elif divide1==0 and divide2==0 and divide3!=0 and divide4==0:
    print (f'Number is divisible by 2,3 and 7 only')
elif divide1!=0 and divide2==0 and divide3==0 and divide4==0:
    print (f'Number is divisible by 3,5 and 7 only')
elif divide1==0 and divide2==0 and divide3==0 and divide4==0:
    print (f'Number is divisible by 2,3,5 and 7')
