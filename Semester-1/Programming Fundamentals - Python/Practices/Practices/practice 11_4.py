from random import *
i=1
while i<=10:
    c=randint(65,90)
    print (chr(c))
    if c==65 or c==69 or c==73 or c==79 or c==85:
        print ('it is vowel')
    else:
        print ('it is consonant')
    i=i+1
