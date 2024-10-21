from random import*
list=[]
for i in range (10):
    x=randint(1,100)
    list.append(x)
sum=0
for i in range (len(list)):
    sum=sum+list[i]
print (f'List: {list}')
print ('Sum of elements:',sum)

