# Task 04: Input previous month budget of an organization for entertainment, which includes cost of milk, tea, 
# sugar and biscuits. Given there is 20% increase in prices. Calculate and print current month budget.

print ('previous month budget')
p_month_milk=int(input('Milk:'))
p_month_sugar=int(input('Sugar:'))
p_month_tea=int(input('Tea:'))
p_month_biscuits=int(input('Biscuits:'))
print (f'TOTAL: {p_month_milk+p_month_sugar+p_month_tea+p_month_biscuits}')

print ('Current month budget')
c_month_milk=int(p_month_milk+(0.20*p_month_milk))
c_month_sugar=int(p_month_sugar+(0.20*p_month_sugar))
c_month_tea=int(p_month_tea+(0.20*p_month_tea))
c_month_biscuits=int(p_month_biscuits+(0.20*p_month_biscuits))
print (f'Milk: {c_month_milk}')
print (f'Sugar: {c_month_sugar}')
print (f'Tea: {c_month_tea}')
print (f'Biscuits: {c_month_biscuits}')
print (f'TOTAL: {c_month_milk+c_month_sugar+c_month_tea+c_month_biscuits}')
