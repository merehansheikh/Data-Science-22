# Task 01: Find quadratic roots with two exceptions:
# - if first parameter (a) is zero, print equation is linear has only one root
# - if discriminant is negative, print roots are imaginary
# - otherwise print both roots

a=int(input('Enter Value of a:'))
b=int(input('Enter Value of b:'))
c=int(input('Enter Value of c:'))
disc=((b*b)-(4*a*c))
square_root_disc=(disc)**(0.5)
x1=-b+square_root_disc/2*a
x2=-b-square_root_disc/2*a
roots=x1,x2
if a==0:
    print ('equation is linear, has one root')
elif disc<=-1:
    print ('roots are imaginary')
else:
    print ('roots=',roots)
