def main_while ():
    n=int(input('N: '))
    i=1
    while i<=n:
        j=1
        while j<=i:
            print (j, end='')
            k=1
            while k<i:
                print (' ', end='')
                k=k+1
            j=j+1
        i=i+1
        print ()
main_while ()

def main_for ():
    n=int(input('N: '))
    for i in range (1,n+1):
        for j in range (1,i+1):
            print (j, end='')
            for k in range (1,i):
                print (' ', end='')
        print ()
main_for ()
