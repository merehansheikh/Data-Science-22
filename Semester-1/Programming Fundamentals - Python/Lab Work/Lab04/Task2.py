amount = int(input('Enter amount deposited: '))



if amount <= 500000:
    amount_one_year = amount+amount*0.07
    print('Amount after one year = ',int(amount_one_year))
    amount_two_year = amount_one_year+amount_one_year*0.07
    print('Amount after two year = ',int(amount_two_year))
    amount_three_year = amount_two_year+amount_two_year*0.07
    print('Amount after three year = ',int(amount_three_year))

    
else:
    amount_one_year = amount+amount*0.10
    print('Amount after one year = ',int(amount_one_year))
    amount_two_year = amount_one_year+amount_one_year*0.10
    print('Amount after two year = ',int(amount_two_year))
    amount_three_year = amount_two_year+amount_two_year*0.10
    print('Amount after three year = ',int(amount_three_year))

    
