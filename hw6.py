import sys

inp = input("Enter Your Letter Here ")
len_check = len(inp)
if len_check == 1:
  ltr = inp
else:
    sys.exit("Please Enter a Valid Letter")
if inp == "a" or inp == "e" or inp == "i" or inp == "o" or inp == "u":
        print("It is a vowel")
else:
        print("It is a consonant")    