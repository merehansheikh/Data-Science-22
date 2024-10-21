from random import*
ch=[]
for i in range (5):
    ch.append(chr(randint(65,90)))
    if ch[i]=='A' or ch[i]=='E' or ch[i]=='I' or ch[i]=='O' or ch[i]=='U':
        ch[i]=chr(randint(65,90))
print (ch)
    
