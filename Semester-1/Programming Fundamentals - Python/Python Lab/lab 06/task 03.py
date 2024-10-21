from random import *
i=1
score=0
while i<=10:
    n1=randint(1,9)
    n2=randint(1,9)
    print (n1)
    print (n2)
    true_sum=n1+n2
    true_diff=0
    if n1>n2:
        true_diff=n1-n2
    else:
        true_diff=n2-n1
    true_prod=n1*n2
    sum=int(input('Enter sum:'))
    if sum==true_sum:
        score=score+1
        difference=int(input('Enter difference:'))
        if difference==true_diff:
            score=score+1
            product=int(input('Enter product:'))
            if product==true_prod:
                score=score+1
            else:
                print ('Wrong')
        elif difference!=true_diff:
            difference=int(input('Wrong, Second chance, Enter difference again:'))
            if difference==true_diff:
                score=score+1
                product=int(input('Enter product:'))
                if product==true_prod:
                    score=score+1
                else:
                    print ('All chances lost, next round')
            elif difference!=true_diff:
                difference=int(input('Wrong difference, Last chance, Enter difference again:'))
                if difference==true_diff:
                   product=int(input('Enter product:'))
                   if product==true_prod:
                       score=score+1
                   elif product!=true_prod:
                        print ('All chances lost, next round')
                else:
                    print ('All chances lost, next round')
    elif sum!=true_sum:
        sum=int(input('Wrong sum, Second chance, Enter sum again:'))
        if sum==true_sum:
            score=score+1
            difference=int(input('Enter difference:'))
            if difference==true_diff:
                product=int(input('Enter product:'))
            elif difference!=true_diff:
                difference=int(input('Wrong difference, Last chance, Enter difference again:'))
                if difference==true_diff:
                    score=score+1
                else:
                    print ('All chances lost, next round')
        elif sum!=true_sum:
            sum=int(input('Wrong sum, Last chance, Enter sum again:'))
            if sum==true_sum:
                score=score+1
            else:
                print ('All chances lost, next round')
        
        i=i+1
print (score)
