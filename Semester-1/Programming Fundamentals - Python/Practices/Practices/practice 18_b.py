r=int(input('Rows: '))
i=1
while i<=r:
    j=1
    while j<=i:
        print ('+', end='')
        j=j+1
    i=i+1
    print()
for a in range (r,1,-1):
    for b in range (a,1,-1):
        print ('+', end='')
    print ()
    
