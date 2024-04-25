"""
Write a method COUNTLINES() in Python to read lines from text file
‘TESTFILE.TXT’ and display the lines which are not starting with any vowel.

"""
"""
def COUNTLINES():
    filename = "TESTFILE.TXT"
    file = open(filename, "r")
    lines = file.readlines()
    number_of_lines=0 
    for i in lines:
        if i[0].lower() not in "AEIOUaeiou":
            number_of_lines = number_of_lines + 1

    print("Answer is: ", number_of_lines)
    file.close

    return ("Program Run")

print(COUNTLINES())
"""



'''
Write a function in Python to read a text file, Alpha.txt and displays
number of  lines which begin with the word ‘You’.
'''
"""
def readYou():
    filename = "alpha.txt"
    file = open(filename, "r")
    lines = file.readlines()
    
    count = 0 
    for i in lines:
        split_line = i.split()
        if(i[0:3].lower()  in "you"):
           count = count + 1

        if split_line[0] == "You":
            print(i)
    print("Answer is: ", count)
    file.close()

print(readYou())
"""
def readYou():
    filename = "alpha.txt"
    file = open(filename, "r")
    lines = file.readlines()
    
    count = 0 
    for i in lines:
        split_line = i.split()
        if(i[0:].lower()  in "aeiouAEIOU"):
           count = count + 1

        if split_line[0] == "aeiouAEIOU":
            print(i)
    print("Answer is: ", count)
    file.close()

print(readYou())