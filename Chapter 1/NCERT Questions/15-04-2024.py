"""
https://ncert.nic.in/textbook.php?lecs1=1-13
"""

"""
#NCERT QUESTION 7
print (" Learning Exceptions...")
try:
 num1= int(input ("Enter the first number"))
 num2=int(input("Enter the second number"))
 quotient=(num1/num2)
 print ("Both the numbers entered were correct")
except ValueError: # to enter only integers
 print (" Please enter only numbers")
except ZeroDivisionError: # Denominator should not be zero
 print(" Number 2 should not be zero")
else:
 print(" Great .. you are a good programmer")
 # to be executed at the end
finally:
    print(" JOB OVER... GO GET SOME REST")


"""
"""
#NCERT QUESTION 9

import math

try:
    num1 = int(input("Enter number: "))
    

except ValueError:
    print("Incorrect values entered! ")

else:
    answer = math.sqrt(num1)
    print("Answer: ", answer)

finally:
    print("Program executed!")

"""