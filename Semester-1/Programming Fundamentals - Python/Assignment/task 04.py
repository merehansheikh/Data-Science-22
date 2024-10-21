from random import*
list1=[6,7,8,9,10]
list2=[1,2,3,4,5]
list3=[]

for i in range (10):
    x=randint(1,10)
    list3.append(x)
new_list=list1+list2+list3
print (f'List 1: {list1}')
print (f'List 2: {list2}')
print (f'List 3: {list3}')
print ('Combined List (not sorted):',new_list)

length=len(new_list)
for i in range(length - 1):
    for j in range(length - i - 1):
        if new_list[j] > new_list[j+1]:
            temp = new_list[j]
            new_list[j], new_list[j+1] = new_list[j+1], temp

print(f'Combined list (sorted): {new_list}')
