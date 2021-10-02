inp = float(input("Enter temperature in celsius "))
out = str((inp * 9/5) + 32)
print(out + "" + " Fahrenheit")

inp = float(input("Enter temperature in fahrenheit "))
out = str((inp - 32) * 5/9)
print(out + "" + " Celsius")