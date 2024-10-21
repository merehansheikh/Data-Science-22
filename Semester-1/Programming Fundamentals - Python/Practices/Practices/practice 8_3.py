# Task 03: Input two characters and check whether they are equal or not by counting bit difference. If bit 
# difference is zero, characters are same, otherwise different


x=ord(input('Enter first character: '))
y=ord(input('Enter second character: '))
i=1
mask=1
count=0
while i<=8:
    if (x&mask==mask and y&mask==mask) or (x&mask==0 and y&mask==0):
        count=count+1
        mask=mask*2
        i=i+1
    else:
        mask=mask*2
        i=i+1
if count==8:
    print (f'\'{chr(x)}\' and \'{chr(y)}\' are same')
else:
    print (f'\'{chr(x)}\' and \'{chr(y)}\' are different')
