amount_deposited = int(input('Amount Deposited: '))

after_one_year = amount_deposited + amount_deposited*0.10

after_two_years = after_one_year + after_one_year*0.10

after_three_years = after_two_years + after_two_years*0.10

print('Amount after one year: ', int(after_one_year))
print('Amount after two years: ', int(after_two_years))
print('Amount after three years: ', int(after_three_years))
