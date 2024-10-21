from random import*
list=[]
i=1
while i<=10:
    x=randint(1,15)
    if x not in list:
        list.append(x)
        i=i+1
print (list)

        
