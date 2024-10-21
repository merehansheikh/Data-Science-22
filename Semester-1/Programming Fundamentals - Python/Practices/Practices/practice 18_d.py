n=int(input('N: '))
for i in range (n):
    for j in range (n,i,-1):
        print ('+',end='')
    for k in range (0,i):
        print (2*' ',end='')
    for j in range (n,i,-1):
        print ('+',end='')
    print ()

for i in range (1,n):
    for j in range (0,i+1):
        print ('+',end='')
    for k in range (i,n-1):
        print (2*' ',end='')
    for j in range (0,i+1):
        print ('+',end='')
    print ()
