eng = int ( input ('Enter English Marks:' ) )
urd = int ( input ('Enter Urdu Marks:' ) )
mat = int ( input ('Enter Maths Marks:' ) )
isl = int ( input ('Enter Islamiat Marks:' ) )
pak = int ( input ('Enter Pak Studies Marks:' ) )
phy = int ( input ('Enter Physics Marks:' ) )
che = int ( input ('Enter Chemistry Marks:' ) )
bio = int ( input ('Enter Biology Marks:' ) )
total = eng + urd + mat + isl + pak + phy + che + bio
print ('  Subject\t  Total\tObtained')
print ('1. English    \t  75\t     ',eng)
print ('2. Urdu       \t  75\t     ',urd)
print ('3. Maths      \t  75\t     ',mat)
print ('4. Islamiat   \t  75\t     ',isl)
print ('5. Pak Studies\t  75\t     ',pak)
print ('6. Physics    \t  75\t     ',phy)
print ('7. Chemistry  \t  75\t     ',che)
print ('8. Biology    \t  75\t     ',bio)
print ('\t Total      \t 525\t    ',total)