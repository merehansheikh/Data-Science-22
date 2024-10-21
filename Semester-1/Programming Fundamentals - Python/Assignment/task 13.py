from random import*
list=[]
for i in range(10):
    list.append(randint(3,7))
    print(list[i],end=' ')
print()
c=0
lc=0
for i in range(len(list)):
    lc=lc+1
    c=0
    d=i
    while(c<3 and d<len(list) and lc<=8):
        print(list[d],end=' ')
        d=d+1
        c=c+1
    print()
