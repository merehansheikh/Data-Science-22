# Task 01: Input a character and tell position of bits, which are on. See sample run:
i=1
mask=1
c=ord(input('Enter a character:'))
while i<=8:
    if c&mask==mask:
        print (f'Bit {i} is on')
    else:
        print (f'Bit {i} is off')
    i=i+1
    mask=mask*2
