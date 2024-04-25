"""
source: https://ncert.nic.in/textbook.php?lecs1=4-13
"""
"""
#NCRT question 8
def Deque():
    return []

def addRear(deque, ch):
    deque.append(ch)

def removeFront(deque):
    if len(deque) == 0:
        return None
    return deque.pop(0)

def removeRear(deque):
    if len(deque) == 0:
        return None
    return deque.pop()

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        addRear(chardeque, ch)
    
    while len(chardeque) > 1:
        first = removeFront(chardeque)
        last = removeRear(chardeque)
        if first != last:
            return False
    return True

string1 = input("Enter a string: ")
palindrome = palchecker(string1.lower())

if palindrome:
    print(string1, "is a palindrome.")
else:
    print(string1, " is not a palindrome.")

"""


"""
#NCERT Question 4

myQueue = []

index = 0

def enqueue(myQueue, element):
    myQueue.append(element)

def isEmpty(myQueue):
    return len(myQueue) == 0

def dequeue(myQueue):
    if not isEmpty(myQueue):
        return myQueue.pop(0)
    else:
        return "Box is empty"

def size(myQueue):
    return len(myQueue)

while True:
    print("\nMenu")
    print("1. Insert a shuttlecock")
    print("2. Remove a shuttlecock")
    print("3. Display the number of shuttlecocks")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        index += 1
        enqueue(myQueue, index)
        print(f"Shuttlecock {index} added.")
    elif choice == 2:
        removed_shuttle = dequeue(myQueue)
        print(f"The shuttlecock removed is: {removed_shuttle}")
    elif choice == 3:
        print(f"The number of shuttlecocks in the box = {size(myQueue)}")
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
"""
