from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	x1 = randint(1, 1000)
	x2 = randint(1, 1000)
	x3 =  randint(1, 1000)
	if x1 > x2:	temp = x1;	x1 = x2;	x2 = temp;
	if x2 > x3:	temp = x2;	x2 = x3;	x3 = temp;
	if x1 > x2:	temp = x1;	x1 = x2;	x2 = temp;
	print (f'Numbers after condition:: {x1}\t\t{x2}\t\t{x3}')

main()