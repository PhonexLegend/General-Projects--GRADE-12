"""
import time

def bubble_sort(elements):
    length_of_list = len(elements)
    print("Length of Elements is: ", length_of_list)
    time.sleep(2)

    for i in range(length_of_list):
        for  j in range(0, length_of_list - i - 1):
            if elements[j] > elements[j+1]:
                elements [j], elements[j+1] = elements[j+1], elements[j]
                
    return elements     
      
elements = list(eval(input("Enter elements: ")))
print("Unorted", elements)
elements = bubble_sort(elements)
print("Sorted list: ", bubble_sort(elements))
"""
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
       
        median = (arr[n // 2 - 1] + arr[n // 2]) // 2
        
    else:
        
        median = arr[n // 2]

    return median



numbers = list(eval(input("Enter elements: ")))


bubble_sort(numbers)


median = find_median(numbers)


print("Sorted list:", numbers)
print("Median:", median)

"""

