def visit_a_and_b(A,B):
    return A & B

def visit_a_or_c(A,C):
    return A ^ C

def update(A,lst):
    for i in lst:
        A.add(i)

def remove(B,lst):
    for user in lst:
        if user in B:
            B.remove(user)
    