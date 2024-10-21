from random import*
length=30
marks=[]
for i in range (length):
    marks.append(randint(1,100))
    print (marks[i],end=' ')
print ()

passed=0
pass_stud=[]
fail_stud=[]
failed=0
sum_pass=0
sum_fail=0
for i in range (length):
    if marks[i]>=50:
        pass_stud.append(marks[i])
        passed+=1
        sum_pass=sum_pass+marks[i]
        print (marks[i],end=' ')
    else:
        fail_stud.append(marks[i])
        failed+=1
        sum_fail=sum_fail+marks[i]
print ()
average=sum_pass//passed
print (f'Averag; {average}')
for i in range (len(fail_stud)):
    print (fail_stud[i],end=' ')
print ()
above_average=[]
below_average=[]
for i in range (len(pass_stud)):
    if pass_stud[i]>average:
        above_average.append(pass_stud[i])
        print (above_average[i],end=' ')
    else:
        below_average.append(pass_stud[i])
print ()
for i in range (len(below_average)):
    print (below_average[i], end=' ')
