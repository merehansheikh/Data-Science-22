from random import *

i=1
score=0
while i<10:
    choice=randint(1,3)
    if choice==1:
        print (f'{i}.Perform Addition')
        n1=randint(0,99)
        n2=randint(0,99)
        print (f'N1: {n1}\nN2: {n2}')
        answer=int(input('Enter Answer:'))
        if answer==n1+n2:
            print ('Correct')
            score=score+1
        else:
            print ('Incorrect')
        print()
    elif choice==2:
        print (f'{i}.Perform Subtraction')
        n1=randint(10,99)
        n2=randint(0,9)
        print (f'N1: {n1}\nN2: {n2}')
        answer=int(input('Enter Answer:'))
        if answer==n1-n2:
            print ('Correct')
            score=score+1
        else:
            print ('Incorrect')
        print()
    elif choice==3:
        print (f'{i}.Perform Multiplication')
        n1=randint(0,9)
        n2=randint(0,9)
        print (f'N1: {n1}\nN2: {n2}')
        answer=int(input('Enter Answer:'))
        if answer==n1*n2:
            print ('Correct')
            score=score+1
        else:
            print ('Incorrect')
        print()
    i=i+1
print (f'Your final score is {score} out of 10')
