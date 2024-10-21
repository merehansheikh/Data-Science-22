from random import*
len=10
list=[[randint(0,9) for j in range(len)]for i in range(len)]
for i in range(len):
    for j in range(len):
        print(list[i][j],end=' ')
    print()
print()
for i in range(len):
    for j in range(len):
        if(list[i][j]==0):
            list[i][j]=1
    for k in range(len):
        print(list[i][k],end=' ')
    print()

