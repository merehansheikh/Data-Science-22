from random import*
num=[]
for i in range (10):
    num.append(randint(1,50))
    if i!=0:
        while (num[i]-num[i-1]) not in range (2,4):
            num[i]=randint(1,100)
print (num)
