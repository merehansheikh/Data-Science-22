rows=int(input())
for i in range (rows):
    for j in range (i):
        print (' ', end='')
    print ('|')
for i in range (rows):
    print (' ', end='')
for i in range (rows):
    print ('-', end='')
print ()
for i in range (rows):
    for j in range (rows,i+1,-1):
        print (' ', end='')
    print ('/')
print ()
