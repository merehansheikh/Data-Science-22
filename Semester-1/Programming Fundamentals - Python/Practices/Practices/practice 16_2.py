# 2. Initialize five elements randomly with 0 or 1. Count how many of them are zero and 
# how many are one.
from random import *
i=1
count_zero=0
count_one=0
while i<=5:
    x=randint(0,1)
    if x==0:
        count_zero+=1
    else:
        count_one+=1
    print (x)
    i=i+1
print (f'count of 1 is {count_one} and count of zero is {count_zero}')
