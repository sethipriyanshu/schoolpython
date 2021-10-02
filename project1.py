grade = ""
print("Project 1 - Average and grade finder")
try:
    sub_1 = float(input(" " + 'Enter Subject 1 Marks Here'))
    sub_2 = float(input(" " + 'Enter Subject 2 Marks Here'))
    sub_3 = float(input(" " + 'Enter Subject 3 Marks Here'))
    sub_4 = float(input(" " + 'Enter Subject 4 Marks Here'))
    sub_5 = float(input(" " + 'Enter Subject 5 Marks Here'))
except:
    print("An error occured , Please try again later")
if sub_1 < 100 and sub_2 < 100 and sub_3 < 100 and sub_4 < 100 and sub_5 < 100:
   sum_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
   average_ =sum_marks / 5
   outa = str(average_)
else:
 print('Marks exceed the maximum limit of 100 , Please Retry')
if average_ >= 90:
    grade = "A"
elif average_ >= 80 and sum_marks < 90:
    grade = "B"
elif average_ >= 70 and sum_marks < 80:
    grade = "C"   
elif average_ >= 60 and sum_marks < 70:
    grade = "D"
elif average_ >= 50 and sum_marks < 60:
    grade = "E"
elif average_ < 50:
    grade = "F"
else :
 print("An unexpected error occured , Try Again")

print ("Your average marks are" + "" + outa)
print("Your grade is " + "" + grade)
 
    