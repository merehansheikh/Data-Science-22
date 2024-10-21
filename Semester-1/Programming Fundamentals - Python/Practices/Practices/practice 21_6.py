from random import*
sum=0
while sum!=50:
    x=randint(1,10)
    sum=sum+x
    print (x, end=' ')
    if sum>50:
        sum=0
        print()
