# Task 02: Input two characters and tell how many bits are same:
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

print (f'In {chr(x)} and {chr(y)}, {count} bit(s) are same')
