side1 = float(input("Enter First Side here "))
side2 = float(input("Enter Second Side here "))
side3 = float(input("Enter Third Side here "))
if side1 == side2 == side3:
    out = "It is an equilateral Triangle"
    print(out)
elif side1 == side2 or side2 == side3 or side3 == side1:
    out = "It is an isoceles Triangle"
    print(out)
else:
    out = "It is a Scalene Triangle"
    print(out)