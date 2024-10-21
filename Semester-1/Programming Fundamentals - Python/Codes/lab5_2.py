from random import *

def main():
    type1 = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if type1 == 0:   type1 = 'D'; clr1 = 'R';
    elif type1 == 1: type1 = 'H'; clr1 = 'R';
    elif type1 == 2: type1 = 'S'; clr1 = 'B';
    else: type1 = 'C'; clr1 = 'B';
    n1 = randint(1, 13)      #card number 1 to three
    print (f'Card 1 has value {n1} and type is {type1}')

    type2 = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if type2 == 0:   type2 = 'D'; clr2 = 'R';
    elif type2 == 1: type2 = 'H'; clr2 = 'R';
    elif type2 == 2: type2 = 'S'; clr2 = 'B';
    else: type2 = 'C'; clr2 = 'B';
    n2 = randint(1, 13)      #card number 1 to three
    print (f'Card 2 has value {n2} and type is {type2}')

    type3 = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if type3 == 0:   type3 = 'D'; clr3 = 'R';
    elif type3 == 1: type3 = 'H'; clr3 = 'R';
    elif type3 == 2: type3 = 'S'; clr3 = 'B';
    else: type3 = 'C'; clr3 = 'B';
    n3 = randint(1, 13)      #card number 1 to three
    print (f'Card 3 has value {n3} and type is {type3}')

    dn12 = (n1 - n2)
    dn13 = (n1 - n3)
    dn23 = (n3 - n2)

    if dn12 < 0: dn12 = -dn12;
    if dn13 < 0: dn13 = -dn13;
    if dn23 < 0: dn23 = -dn23;

    if type1 == type2 and type2 == type3 and ((dn12 == 1 and dn23==1) or (dn12 == 1 and dn13 == 1) or (dn13 == 1 and dn23 == 1)):
       print ('All cards are in sequence and of same type')
    elif type1 == type2 and type2 == type3 and n1 == n2 and n2 == n3:
       print ('All cards have same number and of same type')
    elif type1 == type2 and type2 == type3:
       print ('All cards have same type')
    elif clr1 == clr2 and clr2 == clr3:
       print ('All cards have same color')
    elif (dn12 == 1 and dn23 == 1) or (dn12 == 1 and dn13 == 1) or (dn13 == 1 and dn23 == 1):
       print ('All cards are in sequence')
    elif type1 == type2 or type1 == type3 or type2 == type3:
       print ('Two cards have same type')
    elif dn12 == 1 or dn23 == 1 or dn13 == 1:
       print ('Two cards are in sequence')
    else:
        max = n1
        if max < n2:    max = n2;
        if max < n3:    max = n3;
        print (f'Value of highest card is: {max}')

main()