s=int(input('Enter basic salary:')) # basic salary
m=0.1*s # medical allowance
c=0.15*s # conveyance allowance
h=0.45*s # house rent
g=s+m+c+h # gross salary
g12=g*12 #annual gross
print ('Basic Salary:', s)
print('Medical Allowance:', m)
print('Conveyance Allowance:', c)
print('House Rent:', h)
print('-----------------------------')
print('Gross Salary:', g)
if g12<=200000:
    tax=int(0)
    print ('Less Tax:', tax)
elif g12<=400000:
    tax = 0.1*g
    print ('Less Tax:', tax)
elif g12<=600000:
    tax = 0.15*g
    print ('Less Tax:', tax)
elif g12<=800000:
    tax = 0.20*g
    print ('Less Tax:', tax)
elif g12>800000:
    tax = 0.25*g
    print ('Less Tax:', tax)
print('-----------------------------')
n=g-tax #net salary
print('Net Salary:', n)
