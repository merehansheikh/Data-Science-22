# Task 03: Generate ten set of three random numbers and print their average. Find and print, which of them has 
# highest average.

# Task 04: Repeat task 3 and print, which set has minimum average, and print elements of minimum set. Similarly, 
# print which set has maximum average and print elements of maximum set.

from random import *
i=1
highest=0
lowest=100
set_h=0
set_l=0
min_set1=0
min_set2=0
min_set3=0
max_set1=0
max_set2=0
max_set3=0
while i<=10:
    x=randint(0,100)
    y=randint(0,100)
    z=randint(0,100)
    average=(x+y+z)/3
    if average>highest:
        highest=average
        set_h=i
        max_set1=x
        max_set2=y
        max_set3=z
    if average<lowest:
        lowest=average
        set_l=i
        min_set1=x
        min_set1=y
        min_set1=z
    i=i+1
    print (f'{x}\t{y}\t{z}\t\t{average}')
print (f'Set {set_l} has lowest average')
print (f'Set elements: {min_set1},{min_set2},{min_set3}')
print (f'Set {set_h} has highest average')
print (f'Set elements: {max_set1},{max_set2},{max_set3}')
