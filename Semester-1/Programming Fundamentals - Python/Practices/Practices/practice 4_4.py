# Task 04: Input four random numbers in range 1-100000. Print them. Sort these numbers using one extra 
# variable and conditions. Print them in ascending order, write a single print statement at the end only.

from random import *
x1=randint(1,100000)
x2=randint(1,100000)
x3=randint(1,100000)
x4=randint(1,100000)
if x1>x2:
    x1,x2=x2,x1
if x2>x3:
    x2,x3=x3,x2
if x3>x4:
    x3,x4=x4,x3
if x1>x2:
    x1,x2=x2,x1
if x2>x3:
    x2,x3=x3,x2
if x1>x2:
    x1,x2=x2,x1
print (x1,x2,x3,x4)
