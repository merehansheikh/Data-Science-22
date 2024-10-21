from random import*
len=10
list=[[randint(0,9) for j in range(len)]for i in range(len)]
for i in range(len):
    for j in range(len):
        print(list[i][j],end=' ')
    print()
for i in range(len):
    for j in range(len):
        if(j<i):
            print('  ',end='')
    print(list[i][i])

