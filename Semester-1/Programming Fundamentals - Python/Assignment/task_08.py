from random import*
a=[0]*20
for i in range(len(a)):
    a[i]=randint(1,50)
for i in range(len(a)):
    print(a[i],end=' ')
print()
#sorting list for ascending order values
for i in range(len(a)):
    temp=0
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
for i in range(len(a)):
    print(a[i],end=' ')
print()
#sorting for unique values
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            while(a[i]==a[j]):
               a[j]=randint(1,50)
#for i in range(len(a)):
    #print(a[i],end=' ')
#print()
    

for i in range(len(a)):
    temp=0
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
for i in range(len(a)):
    print(a[i],end=' ')
print()
print()
c=1
for i in range(len(a)):
    c=a[i]
    for j in range(i+1,i+2):
        if(j<len(a)):
            while(c<a[j]):
                c=c+1
                if(c<a[i+1]):
                    print(c,end=' ')
        
        















        
    
