from random import *
i=1
passed=0
failed=0
mid_total=0
final_total=0
sessional_total=0
overall_total=0
max_all=0
max_mid=0
max_final=0
max_sessional=0
min_all=100
min_mid=35
min_final=40
min_sessional=25

print (f'Roll No.\tMid\tFinal\tSessional\tTotal\tGrade')
while i<=30:
    mid=randint(0,35)
    final=randint(0,40)
    sessional=randint(0,25)
    total=mid+final+sessional
    grade=()
    if total>=85:
        grade='A'
    elif total>=80:
        grade='A-'
    elif total>=75:
        grade='B+'
    elif total>=70:
        grade='B'
    elif total>=65:
        grade='B-'
    elif total>=61:
        grade='C+'
    elif total>=58:
        grade='C'
    elif total>=55:
        grade='C-'
    elif total>=50:
        grade='D'
    else:
        grade='F'
    if total>=50:
        passed=passed+1
    else:
        failed=failed+1
    mid_total+=mid
    final_total+=final
    sessional_total+=sessional
    overall_total+=total
    if mid>max_mid:
        max_mid=mid
    if final>max_final:
        max_final=final
    if sessional>max_sessional:
        max_sessional=sessional
    if total>max_all:
        max_all=total
    if mid<min_mid:
        min_mid=mid
    if final<min_final:
        min_final=final
    if sessional<min_sessional:
        min_sessional=sessional
    if total<min_all:
        min_all=total
    print (f'{i}\t\t{mid}\t{final}\t{sessional}\t\t{total}\t{grade}')
    i=i+1
print (f'Total: {i}')
print (f'Pass: {passed}')
print (f'Fail: {failed}')
print (f'Overall Average Marks: {overall_total/i}')
print (f'Average Midterm Marks: {mid_total/i}')
print (f'Average Sessional Marks: {sessional_total/i}')
print (f'Average Final Total Marks: {final_total/i}')
print (f'Maximum Marks: {max_all}')
print (f'Maximum Midterm Marks: {max_mid}')
print (f'Maximum Sessional Marks: {max_sessional}')
print (f'Maximum Final Marks: {max_final}')
print (f'Minimum Marks: {min_all}')
print (f'Minimum Midterm Marks: {min_mid}')
print (f'Minimum Sessional Marks: {min_sessional}')
print (f'Minimum Final Marks: {min_final}')
