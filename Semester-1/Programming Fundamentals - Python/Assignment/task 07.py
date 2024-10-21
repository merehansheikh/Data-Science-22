from random import*
list=[]
for i in range(10):
    list.append(randint(1,15))
    print(list[i],end=' ')
print()
print('indexes of same elements:')
for i in range(len(list)):
    c=0
    for j in range(i+1,len(list)):
        if(list[i]==list[j] and list[j]!=-1):
            
            c=c+1
            if(c==1):
                print(i,end=' ')
            print(j,end=' ')
            list[j]=-1
    if i==1:
        print()
    
