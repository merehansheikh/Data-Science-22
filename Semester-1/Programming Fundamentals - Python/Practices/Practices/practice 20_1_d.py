def print_quad_roots(a,b,c):
    disc=(b**2)-4*a*c
    disc=disc**(1/2)
    x1=(-b+disc)/(2*a)
    x2=(-b-disc)/(2*a)
    print (x1)
    print (x2)
print_quad_roots(11,-2,-9)
