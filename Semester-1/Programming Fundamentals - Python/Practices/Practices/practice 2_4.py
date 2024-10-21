# Task 04: Input number of seconds and print number of hours, number of minutes and remaining number of 
# seconds: (Hint: Use integer division and remainder operator.

seconds=int(input('Enter seconds:'))
hours=seconds//3600
minutes=seconds%3600
minutes=minutes//60
seconds=minutes%60
print(f'Number of hours: {hours}\nNumber of minutes: {minutes}\nNumber of seconds: {seconds}')
