from random import*
list=[]
for i in range(20):
    list.append(randint(0,9))
print(list)
copy_list=[list[i] for i in range(len(list))]
for i in range(2,len(list)-2):
    list[i]=(list[i-1]+list[i-2]+list[i+1]+list[i+2])//4
for i in range(len(list)):
    print(list[i],end=' ')
