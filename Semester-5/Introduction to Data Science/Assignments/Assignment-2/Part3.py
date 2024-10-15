def visit_a_and_b(A,B):
    return A & B

#Sample Run
A = {1,2,3,4,5,6,7,8,9,10}
B = {1,3,5,6,7,8,11,12,45}

print(visit_a_and_b(A,B))

def visit_a_or_c(A,C):
    return A ^ C

#Sample Run
A = {1,2,3,4,5,6,7,8,9,10}
C = {21,22,1,6,7,25,15,16}

print(visit_a_or_c(A,C))

def update(A,lst):
    for i in lst:
        A.add(i)
    return A

#Sample Run
A = {1,2,3,4,5,6,7,8,9,10}
l = [1,11,21,31,41,51]

print(update(A,l))

def remove(B,lst):
    for user in lst:
        if user in B:
            B.remove(user)
    return B

#Sample Run
B = {1,3,5,6,7,8,11,12,45}
l = [1,11,21,31,41,51]

print(remove(B,l))