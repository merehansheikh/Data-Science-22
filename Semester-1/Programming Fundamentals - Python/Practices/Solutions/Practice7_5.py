from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	n = randint(1, 30)
	print (f'Number: {n}')
	if n % 3 == 0 and n % 7 == 0:
		print ('Number is divisible by both 3 and 7\n')
	elif n % 3 == 0 and n % 5 == 0:
		print ('Number is divisible by both 3 and 5\n')
	elif n % 3 == 0 and n % 2 == 0:
		print ('Number is divisible by both 2 and 3\n')
	elif n % 5 == 0 and n % 2 == 0:
		print ('Number is divisible by both 2 and 5\n')
	elif n % 7 == 0 and n % 2 == 0:
		print ('Number is divisible by both 2 and 7\n')
	elif n % 3 == 0:
		print ('Number is divisible by 3 only\n')
	elif n % 2 == 0:
		print ('Number is divisible by 2 only\n')
	elif n % 5 == 0:
		print ('Number is divisible by 5 only\n')
	elif n % 7 == 0:
		print ('Number is divisible by 7 only\n')
	else:
		print ('Number is not divisible by 2, 3, 5 & 7\n')

main()