i=1
while i<=99:
    x=i
    sum=(x//10)+(x%10)
    if x<10:
        print (f'[{x}]', end=' ')
    elif sum<10:
        print (f'[{x} {sum}]', end=' ')
    else:
        print (f'[{x} {sum} {(sum//10)+(sum%10)}]', end=' ')
    i=i+1
