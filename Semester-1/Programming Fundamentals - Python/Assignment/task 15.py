from random import*
len=10
list=[[randint(0,9) for j in range(len)]for i in range(len)]
for i in range(10):
    for j in range(10):
        print(list[i][j],end=' ')
    print()
print()
for i in range(10):
    for j in range(10):
        if(list[i][j]==0):
            print(i,' ',j)
            

