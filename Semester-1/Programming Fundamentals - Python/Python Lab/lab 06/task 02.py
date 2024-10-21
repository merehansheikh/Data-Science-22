def main ():
    i=1    
    while i<=100:
        x=i
        tens=x//10
        units=x%10
        if units==1:
            units='one'
        elif units==2:
            units='two'
        elif units==3:
            units='three'
        elif units==4:
            units='four'
        elif units==5:
            units='five'
        elif units==6:
            units='six'
        elif units==7:
            units='seven'
        elif units==8:
            units='eight'
        elif units==9:
            units='nine'
        if tens==2:
            tens='twenty'
        elif tens==3:
            tens='thirty'
        elif tens==4:
            tens='forty'
        elif tens==5:
            tens='fifty'
        elif tens==6:
            tens='sixty'
        elif tens==7:
            tens='seventy'
        elif tens==8:
            tens='eighty'
        elif tens==9:
            tens='ninety'
        elif tens==10:
            tens='hundred'
        if x<10:
            print (units)
        if x==10:
            print ('ten')
        if x==11:
            print ('eleven')
        elif x==12:
            print ('twelve')
        elif x==13:
            print ('thirteen')
        elif x==14:
            print ('fourteen')
        elif x==15:
            print ('fifteen')
        elif x==16:
            print ('sixteen')
        elif x==17:
            print ('seventeen')
        elif x==18:
            print ('eighteen')
        elif x==19:
            print ('nineteen')
        if x>=20<99:
            if units==0:
                print (tens)
            else:
                print (tens, units)
        i=i+1
main ()
