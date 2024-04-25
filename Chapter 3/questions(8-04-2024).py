"""
def display(stk):
    if stk==[]:
        print("Stack is Empty")
    else:
        top = len(stk)-1
        print(stk[top],"-Top")
        for i in range(top-1,-1,-1):
            print(stk[i])

stk = []
display(stk)
"""
"""
def push(stk,e):
    stk.append(e)
    top = len(stk)-1
    print(stk)

stk = []
e = 7, 8, 9
push(stk, e)

"""
"""
data = {}

def user_input():
    number_of_enteries = int(input("Enter no. of students: "))
    for i in range(number_of_enteries):

        name = input("Enter name: ")
        marks = int(input("Enter Marks: "))
        data[name] = marks
        print(data)

for i in data:
    print(data[i])
    if data[i] > 70:
        
        print(i)

    else:
        print("No value of 70")

user_input()

"""