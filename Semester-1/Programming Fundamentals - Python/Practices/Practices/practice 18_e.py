n=int(input('N: '))
for i in range (1,n):
    c=97
    print (chr(c),end=' ')
    c=c+i
    for j in range (n):
        print (chr(c),end=' ')
        c=c+i
    print ()
