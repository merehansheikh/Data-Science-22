from random import*
list=[]
for i in range (10):
    x=randint(1,100)
    list.append(x)
print ('List:', list)
print (f'Reverse:', end=" ")
index=len(list)-1
for i in range(len(list)):
    print (list[index], end=" ")
    index=index-1
