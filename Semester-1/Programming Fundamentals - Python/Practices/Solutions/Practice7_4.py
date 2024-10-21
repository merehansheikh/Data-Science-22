	m2 = randint(0, 100)
	print (f'Marks 1: {m1}\nMarks 2: {m2}')
	if m1 == m2:
		print ('SAME\n')
	elif (m1 < 50 and m2 < 50) or (m1 >= 50 and m1 < 55 and m2 >= 50 and m2 < 55) or (m1 >= 55 and m1 < 58 and m2 >= 55 and m2 < 58) or (m1 >= 58 and m1 < 61 and m2 >= 58 and m2 < 61) or (m1 >= 61 and m1 < 65 and m2 >= 61 and m2 < 65)  or (m1 >= 65 and m1 < 70 and m2 >= 65 and m2 < 70) or (m1 >= 70 and m1 < 75 and m2 >= 70 and m2 < 75)  or (m1 >= 75 and m1 < 80 and m2 >= 75 and m2 < 80) or (m1 >= 80 and m1 < 85 and m2 >= 80 and m2 < 85) or (m1 >= 85 and m2 >= 85):
		print ('ALMOST SAME\n')
	else:
		print ('DIFFERENT\n')


main()
