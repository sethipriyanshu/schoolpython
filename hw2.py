leap = int(input("Enter the year here"))
if leap % 4 == 0:
   if (leap % 100) == 0:  
       if (leap % 400) == 0:  
           print(" It is a leap year")  
       else:  
           print("It is not a leap year")  
   else:  
       print("It is a leap year")  
else:  
   print("It is not a leap year")  