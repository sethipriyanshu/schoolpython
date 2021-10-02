ang1 = float(input("Enter First Angle in degrees "))
ang2 = float(input("Enter Second Angle in degrees "))
ang3 = float(input("Enter Third Angle in degrees"))
ang_add = ang1 + ang2 + ang3
if ang_add == 180:
    print("Yes! This Triangle is possible")
else:
    print("No! This Triangle is not possible")
    