from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	n1 = randint(1, 5)
	n2 = randint(1, 5)
	print (f'First Number: {n1}\nSecond Number: {n2}')
	if n1 == n2:
	    print ('Numbers are exactly equal')
	elif n1+1 == n2 or n1 == n2+1:
	    print ('Numbers are almost equal\n')	
	else:
	    print ('Numbers are not equal\n')
main()

