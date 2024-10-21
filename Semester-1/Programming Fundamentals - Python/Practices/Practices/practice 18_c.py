n=int(input('N: '))
for i in range (n+1,1,-1):
    for j in range (i,n+1):
        print (' ',end='')
    for j in range (i,1,-1):
        print ('+',end='')
    print ()
for i in range (n,1,-1):
    for j in range (1,i-1):
        print (' ',end='')
    for j in range (i,n+2):
        print ('+',end='')
    print ()
        
