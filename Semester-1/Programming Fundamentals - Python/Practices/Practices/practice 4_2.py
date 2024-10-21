from random import *
number=randint(1,10)
i=1
while i<=3:
    guess=int(input('Enter your guess between 1 to 10:'))
    if guess==number:
        print('"Winner"')
        i=5
    else: 
        i=i+1
        print ('Wrong guess! \n' , end=' ')
if i==4:
    print ('You lose')


