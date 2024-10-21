basic_salary = int(input('Basic Salary: '))

medical_allowance = basic_salary*0.10
conven_allowance = basic_salary*0.15
house_rent = basic_salary*0.45

gross_salary = basic_salary+medical_allowance+conven_allowance+house_rent

net_salary = gross_salary*12


if net_salary<=200000:
    tax = 0
    #print('Tax = ',tax)
elif net_salary>200000 and net_salary<400000:
    tax = gross_salary*0.10
    #print('Tax = ',tax)
elif net_salary>400000 and net_salary<600000:
    tax = gross_salary*0.15
    #print('Tax = ',tax)
elif net_salary>600000 and net_salary<800000:
    tax = gross_salary*0.20
    #print('Tax = ',tax)
elif net_salary>800000:
    tax = gross_salary*0.25
    #print('Tax = ',tax)



    
net_salar = gross_salary -tax

print('Basic salary: ',basic_salary)
print('Medical Allowance: ',medical_allowance)
print('Convenyence Allowance: ',conven_allowance)

print('House Rent: ',house_rent)
print('-------------------------------------------')
print('Gross Salary: ',gross_salary)
print('Less Tax: ',tax)
print('-------------------------------------------')
print('Net Salary: ',net_salar)
print('-------------------------------------------')

    
