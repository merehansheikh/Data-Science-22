from random import*
x=[]
sum=0
for i in range (10):
    x.append(randint(1,100))
    print (x[i], end=' ')
    sum=sum+x[i]
print ()
average=sum//10
print ('Average: ',average)
y=[]
count_p=0
count_n=0
for i in range (10):
    y.append(average-x[i])
    print (y[i],end=' ')
    if y[i]<0:
        count_n+=1
    elif y[i]>0:
        count_p+=1
print ()
print ('Count Positive: ', count_p)
print ('Count Negative: ', count_n)
