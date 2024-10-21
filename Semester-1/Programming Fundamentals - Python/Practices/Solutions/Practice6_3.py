from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	m = randint(0, 100)
	print(f'Marks: {m}\nGrade: ', end='')
	if (m < 50):			print('F\n');	
	elif (m < 55):	print('D\n');	
	elif (m < 58):	print('C-\n');	
	elif (m < 61):	print('C\n');
	elif (m < 65):	print('C+\n');	
	elif (m < 70):	print('B-\n');	
	elif (m < 75):	print('B\n');
	elif (m < 80):	print('B+\n');	
	elif (m < 85):	print('A-\n');	
	else:				print('A\n');

main()