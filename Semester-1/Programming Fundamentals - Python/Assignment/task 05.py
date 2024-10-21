from random import *
list=[]
for i in range (10):
    list.append(randint(1,100))
print (f'Parent List: {list}')
count_even=0
print ('Even Numbers: ', end='')
for i in range (len(list)):
    if (list[i]%2==0):
        print (list[i], end=' ')
        count_even+=1
print ()
count_odd=0
print ('Odd Numbers: ', end='')
for i in range (len(list)):
    if (list[i]%2!=0):
        print (list[i], end=' ')
        count_odd+=1
print ()
for i in range (len(list)):
    if count_even!=count_odd:
        if count_even>count_odd:
            if (list[i]%2!=0):
                list[i]+=1
        else:
            if (list[i]%2==0):
                list[i]-=1
print ('Final List: ', end='')
for i in range (len(list)):
    print (list[i], end=' ')
                
