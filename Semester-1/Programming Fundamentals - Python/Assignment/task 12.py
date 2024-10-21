from random import*
list=[]
for i in range(10):
    list.append(randint(3,7))
    print(list[i],end=' ')
print()
for i in range(len(list)):
    sum=0
    d=0
    while(d<=i):
        print(list[d],end=' ')
        sum=sum+list[d]
        d=d+1
    print('= ',sum)
