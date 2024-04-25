"""
Source: https://ncert.nic.in/textbook.php?lecs1=3-13
"""
"""
#NCERT QUESTION 2(a)
result=0
numberList=[10,20,30]
numberList.append(40)
result=result+numberList.pop()
result=result+numberList.pop()
print(“Result=”,result

"""
"""
#NCERT Question 2(b)
answer=[]; output=''
answer.append('T')
answer.append('A')
answer.append('M')
ch=answer.pop()
output=output+ch
ch=answer.pop()
output=output+ch
ch=answer.pop()
output=output+ch
print(“Result=”,output)
"""
"""
#NCERT Question 3

def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

user_input = input("Enter a string: ")
reversed_result = reverse_string(user_input)
print("Reversed string: ",  reversed_result)
"""

#NCERT Question  7

n = int(input("Enter the number of values: "))
stack = [] 
for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 != 0:  
        stack.append(num)

largestNum = stack.pop()

while len(stack) > 0:
    num = stack.pop()
    if num > largestNum:
        largestNum = num

print("The largest odd number found is:", largestNum)

