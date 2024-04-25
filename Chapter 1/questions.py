"""
def average_of_three_numbers(n1, n2, n3):
    
    avg = (n1+n2+n3)/3

    return avg

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second Number: "))
n3 = int(input("Enter second Number: "))
print(average_of_three_numbers(n1, n2, n3))
"""
"""
for i in range(1, 11):
    print(i)
    
print("____________________")

for j in range(10, 0, -1):
   print(j)

"""

"""
def even_or_odd(num):
    if (num % 2) == 0:
        print("Even")

    else:
        print("odd")

    return ("")
num = int(input("Enter number: "))
print(even_or_odd(num))
"""


def comparison(string1, string2):

    len1 = len(string1)
    print(len1, "is lenghth of string one")

    len2 = len(string2)
    print(len2, "is length of string two")

    if len1 > len2:
        print("Length of string 1 is more")

    elif len1 < len2:
        print("Length of string 2 is more")

    else:
        print("Length is equal")

    return ("")

string1 = input("Enter first string string: ")
string2 = input("Enter second string: ")
print(comparison(string1, string2))
