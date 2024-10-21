# Task 04: Input marks of two numbers, check and print 'SAME', 'ALMOST SAME' and 'DIFFERENT'. If both
# marks are equal, print 'SAME'. If both marks are different but have same grades, print 'ALMOST
# SAME',otherwise print 'DIFFERENT' [Use grade table shared in practice 6]

marks1 = int(input('Marks 1:'))
marks2 = int(input('Marks 2:'))
grade1 = ()
grade2 = ()
if marks1>=85:
    grade1='A'
elif marks1>=80:
    grade1='A-'
elif marks1>=75:
    grade1='B+'
elif marks1>=70:
    grade1='B'
elif marks1>=65:
    grade1='B-'
elif marks1>=61:
    grade1='C+'
elif marks1>=58:
    grade1='C'
elif marks1>=55:
    grade1='C-'
elif marks1>=50:
    grade1='D'
elif marks1<50:
    grade1='F'
if marks2>=85:
    grade2='A'
elif marks2>=80:
    grade2='A-'
elif marks2>=75:
    grade2='B+'
elif marks2>=70:
    grade2='B'
elif marks2>=65:
    grade2='B-'
elif marks2>=61:
    grade2='C+'
elif marks2>=58:
    grade2='C'
elif marks2>=55:
    grade2='C-'
elif marks2>=50:
    grade2='D'
elif marks2<50:
    grade2='F'
if marks1==marks2:
    print ('SAME')
elif grade1==grade2:
    print ('ALMOST EQUAL')
else:
    print ('NOT EQUAL')
