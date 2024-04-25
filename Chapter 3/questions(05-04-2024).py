"""
st = []
def push(st):
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter name: ")
        st.append(name)
    print(st)

def pop(st):
    if(st == []):
        print("Stack is empty!")

    else:
        deleted = st.pop()
        print("removed ", deleted)
        print("Deleted student")

    
    
def search(st):
    print(st)
   
    name_index = int(input("Enter index: "))
    print(st[name_index])

  

    

push(st)
pop(st)
search(st)

"""
"""
information = []

def push(information):
    number_of_enteries = int(input("Enter  number of enteries: "))
    hostel_number = int(input("Enter hostel number: "))
    for i in number_of_enteries:
        name = input("Name: ")
        
        room_no = int(input("Enter room number: "))

        information
"""
