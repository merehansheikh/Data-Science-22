from random import*
list=[]
for i in range(10):
    list.append(randint(3,7))
print(list)
for i in range(len(list)):
    c=0
    while(c<list[i]):
        print('*',end=' ')
        c=c+1
    print()
