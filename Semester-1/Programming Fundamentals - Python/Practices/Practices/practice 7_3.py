from random import *

def main ():
    x1 = randint(1,1000)
    x2 = randint(1,1000)
    x3 = randint(1,1000)
    print (x1, x2, x3)
    if x1<x2<x3:
        print ('Numbers are in order')
    else:
        print ('Numbers are out of order')
main()
main()
main()
main()
