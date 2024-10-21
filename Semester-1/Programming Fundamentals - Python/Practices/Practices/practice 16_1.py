# 1. Input ten elements and Find second smallest element?
i=1
lowest=0
lowest2:1
while i<=10:
    x=int(input('Number:'))
    if i==1:
        lowest=x
    elif i==2:
        lowest2=x
        if lowest>lowest2:
            lowest,lowest2=lowest2,lowest
    elif x<lowest2 and x>lowest:
        lowest2=x
    elif x<lowest:
        lowest2=lowest
    i=i+1
print (f'Second Smallest number is: {lowest2}')
    
    
