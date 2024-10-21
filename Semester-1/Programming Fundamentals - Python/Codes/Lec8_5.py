s=input ('Enter Alphabet: ')
if s >= 'A' and s<='Z':
    print (f'{s} is capital letter')
    print(f'Small letter of {s} is: ', chr(ord(s) + 32))
if s >= 'a' and s <= 'z':
    print (f'{s} is small letter')
    print (f'Capital letter of {s} is: ', chr (ord(s) - 32 ))
