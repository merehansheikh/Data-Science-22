
	x2 = randint(1, 1000)
	x3 =  randint(1, 1000)
	x4 =  randint(1, 1000)
	print (f'Numbers before condition:: {x1}\t\t{x2}\t\t{x3}\t\t{x4}')
	if x1 > x2:	temp = x1;	x1 = x2;	x2 = temp;
	if x2 > x3:	temp = x2;	x2 = x3;	x3 = temp;
	if x3 > x4:	temp = x3;	x3 = x4;	x4 = temp;
	if x1 > x2:	temp = x1;	x1 = x2;	x2 = temp;
	if x2 > x3:	temp = x2;	x2 = x3;	x3 = temp;
	if x1 > x2:	temp = x1;	x1 = x2;	x2 = temp;
	print (f'Numbers after condition:: {x1}\t\t{x2}\t\t{x3}\t\t{x4}')

main()