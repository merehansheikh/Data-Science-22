s=input ('Enter Alphabet: ')
#without if-else
print(f'Small letter of {s} is: ', chr(ord(s) | 32))
print (f'Capital letter of {s} is: ', chr (ord(s) & ~32 ))#Don't worry about ~32, I will discuss in next class

