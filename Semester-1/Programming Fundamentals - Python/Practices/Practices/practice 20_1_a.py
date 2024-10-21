def print_rectangular_box(rows, cols):
    for i in range (rows):
        print ('*', end='')
        for j in range (cols-2):
            if i==0 or i==rows-1:
                print ('*', end='')
            else:
                print (end=' ')
        print ('*', end='')
        print ()
print_rectangular_box(5,10)
            
    
