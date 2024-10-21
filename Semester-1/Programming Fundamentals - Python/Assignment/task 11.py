from random import*
list=[]
for i in range(10):
    list.append(randint(3,7))
    print(list[i],end=' ')
print()
for i in range(len(list)):
    d=0
    while(d<=i):
        print(list[d],end=' ')
        d=d+1
    print()
