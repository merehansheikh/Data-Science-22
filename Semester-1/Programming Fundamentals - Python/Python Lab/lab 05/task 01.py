from random import *
x=randint(20,99)
tens=x//10
units=x%10
if tens==2:
    tens='twenty'
elif tens==3:
    tens='thirty'
elif tens==4:
    tens='fourty'
elif tens==5:
    tens='fifty'
elif tens==6:
    tens='sixty'
elif tens==7:
    tens='seventy'
elif tens==8:
    tens='eighty'
elif tens==9:
    tens='ninety'
if units==0:
    unist=''
elif units==1:
    units='one'
elif units==2:
    units='two'
elif units==3:
    units='three'
elif units==4:
    units='four'
elif units==5:
    units='five'
elif units==6:
    units='six'
elif units==7:
    units='seven'
elif units==8:
    units='eight'
elif units==9:
    units='nine'
print (f'Number {x} in english is {tens} {units}')
