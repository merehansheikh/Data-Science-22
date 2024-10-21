from random import*
x=randint(1,50)
y=randint(1,50)
i=0
while x+y!=50:
    x=randint(1,50)
    y=randint(1,50)
    i+=1
print (i, x, y, x+y)
