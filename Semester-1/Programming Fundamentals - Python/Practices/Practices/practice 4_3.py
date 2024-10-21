from random import *
x1=randint(1,10)
x2=randint(1,10)
x3=randint(1,10)
if x1>x2:
    x1,x2=x2,x1
elif x2>x3:
    x2,x3=x3,x2
elif x1>x2:
    x1,x2=x2,x1
print (x1,x2,x3)
if x2-x1>=2 and x3-x2>=2 and x3-x1>=2:
    print ('OK')
else:
    print ('Sorry')
