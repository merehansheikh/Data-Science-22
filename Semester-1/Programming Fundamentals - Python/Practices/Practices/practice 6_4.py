# Q4. A shop keeper has pack of 6 eggs and he sells eggs in packs, customer has to purchase number of packs 
# according to their requirements. Write a program to input number of eggs and print minimum number of packs 
# required by the customer?

eggs=int(input('Eggs: '))
packs=eggs//6
additional=eggs%6
if additional==0:
    packs=packs
else:
    packs=packs+1
print (f'Packs: {packs}')
