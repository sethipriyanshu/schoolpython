import sys

mark_1 = float(input("Enter Subject 1 Marks Here"))
mark_2 = float(input("Enter Subject 2 Marks Here"))
mark_3 = float(input("Enter Subject 3 Marks Here"))
mark_4 = float(input("Enter Subject 4 Marks Here"))
mark_5 = float(input("Enter Subject 5 Marks Here"))
mark_sum = mark_1 + mark_2 + mark_3 + mark_4 + mark_5
mark_perc = (mark_sum / 500) * 100
if mark_sum > 500:
    sys.exit("Please Enter Valid Marks")
elif mark_sum >= 80:
    print("Your Grade is A and your percentage is " + str(mark_perc) + "%")
elif mark_sum >= 60 and mark_sum < 80:
     print("Your Grade is B and your percentage is " + str(mark_perc) + "%")
elif mark_sum >= 50 and mark_sum < 60:
     print("Your Grade is C and your percentage is " + str(mark_perc) + "%")
elif mark_sum >= 45 and mark_sum < 50:
     print("Your Grade is D and your percentage is " + str(mark_perc) + "%")
elif mark_sum >= 25 and mark_sum < 45:
     print("Your Grade is E and your percentage is " + str(mark_perc) + "%")
else:
     print("Your Grade is F and your percentage is " + str(mark_perc) + "%")