# this code shows ninth class marks sheet
english_total=75
english_obtained=int(input('Enter obtained marks in English:'))
urdu_total=75
urdu_obtained=int(input('Enter obtained marks in Urdu:'))
maths_total=75
maths_obtained=int(input('Enter obtained marks in Maths:'))
islamiat_total=50
islamiat_obtained=int(input('Enter obtained marks in Islamiat:'))
pakstudies_total=50
pakstudies_obtained=int(input('Enter obtained marks in Pak Studies:'))
physics_total=75
physics_obtained=int(input('Enter obtained marks in Physics:'))
chemistry_total=75
chemistry_obtained=int(input('Enter obtained marks in Chemistry:'))
biology_total=75
biology_obtained=int(input('Enter obtained marks in Biology:'))
total_marks=english_total+urdu_total+maths_total+islamiat_total+pakstudies_total+physics_total+chemistry_total+biology_total
obtained_marks=english_obtained+urdu_obtained+maths_obtained+islamiat_obtained+pakstudies_obtained+physics_obtained+chemistry_obtained+biology_obtained
percentage=(obtained_marks/total_marks)*100
print(f'Subject\t\tTotal\tObtained')
print(f'1.English\t{english_total}\t{english_obtained}')
print(f'2.Urdu\t\t{urdu_total}\t{urdu_obtained}')
print(f'3.Maths\t\t{maths_total}\t{maths_obtained}')
print(f'4.Islamiat\t{islamiat_total}\t{islamiat_obtained}')
print(f'5.Pak Studies\t{pakstudies_total}\t{pakstudies_obtained}')
print(f'6.Physics\t{physics_total}\t{physics_obtained}')
print(f'7.Chemistry\t{chemistry_total}\t{chemistry_obtained}')
print(f'8.Biology\t{biology_total}\t{biology_obtained}')
print(f'TOTAL\t\t{total_marks}\t{obtained_marks}')
print(f'Percentage Marks: {percentage}')
