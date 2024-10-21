Deposit=int(input('Enter Amount Deposited:'))
if Deposit<=500000:
    interest=0.07*Deposit
    after_one_year=Deposit+interest
    after_two_years=after_one_year+(after_one_year*0.07)
    after_three_years=after_two_years+(after_two_years*0.07)
    print ('Amount after one year:', after_one_year)
    print ('Amount after two years:', after_two_years)
    print ('Amount after three years:', after_three_years)
else:
    interest=0.1*Deposit
    after_one_year=Deposit+interest
    after_two_years=after_one_year+(after_one_year*0.1)
    after_three_years=after_two_years+(after_two_years*0.1)
    print ('Amount after one year:', after_one_year)
    print ('Amount after two years:', after_two_years)
    print ('Amount after three years:', after_three_years)
    
