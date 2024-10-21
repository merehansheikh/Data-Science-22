# Task 04: Input a character and bit position from user and check, whether the bit is on or off
x=ord(input('Enter a character: '))
bit=int(input('Enter bit number: '))
mask=2**(bit-1)
if x&mask==mask:
    print (f'The bit number {bit} is on in {chr(x)}')
else:
    print (f'The bit number {bit} is off in {chr(x)}')
