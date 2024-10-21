b_salary = int(input('Basic salary: '))

medical_allowance = b_salary*10//100

conveyance_allowance = b_salary*15//100

house_rent = b_salary*45//100

gross_salary = b_salary + medical_allowance +house_rent + conveyance_allowance

tax = gross_salary*10//100
net_salary = gross_salary - tax

print('Gross Salary: ', gross_salary)
print('net salary:   ',net_salary)
