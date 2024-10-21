# Task 03: Generate ten set of three random numbers and print their average. Find and print, which of them has 
# highest average.

from random import *
i=1
highest=0
set=0
while i<=10:
    x=randint(0,100)
    y=randint(0,100)
    z=randint(0,100)
    average=(x+y+z)/3
    if average>highest:
        highest=average
        set=i
    i=i+1
    print (f'{x}\t{y}\t{z}\t\t{average}')
print (f'Set {set} has highest average')
        
