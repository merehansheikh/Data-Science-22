rows=int(input())
cols=int(input())
for i in range (cols):
    print ('o', end='')
for i in range (rows):
    print (end=' ')
for i in range (cols):
    print ('o', end='')
print ()


for i in range (rows):
    for j in range (cols):
        print (end=' ')
    for j in range (cols,i+cols):
        print (end=' ')
    print ('o')
    
for i in range (rows):
    for j in range (cols):
        print (end=' ')
    for j in range (i+cols,cols,-1):
        print (end=' ')
    print ('o')
    
print ()
for i in range (cols):
    print ('o', end='')
for i in range (rows):
    print (end=' ')
for i in range (cols):
    print ('o', end='')
