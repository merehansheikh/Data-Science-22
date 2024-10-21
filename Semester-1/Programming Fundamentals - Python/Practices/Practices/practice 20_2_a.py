def middle_value(x,y,z):
    mid=0
    if (y>x and y<z) or (y<x and y>z):
        mid=y
    elif (x>y and x<z) or (x<y and x>z):
        mid=x
    else:
        mid=z
    return mid
print (middle_value(9,8,5))
