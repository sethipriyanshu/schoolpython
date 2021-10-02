num1 = int(input(("Enter First Number Here")))
num2 = int(input(("Enter Second Number Here")))
num3 = int(input(("Enter Third Number Here")))

if num1 > num2 and num1 > num3:
    out = "Number 1 is the greatest among three numbers11"
elif num2 > num1 and num2 > num3:
    out = "Number 2 is the greatest among three numbers"
elif num3 > num1 and num3 > num2:
    out = "Number 3 is the greatest among three numbers"
else:
    out = "Invalid inputs , Try Again"
    
print(out)