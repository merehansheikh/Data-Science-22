from random import*
list1=[]
list2=[]
for i in range (10):
    x=randint(1,100)
    list1.append(x)
for i in range (len(list1)):
    list2.append(list1[i])
print (f'List 1: {list1}')
print (f'List 2: {list2}')
