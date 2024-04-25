"""
def validator(m):
    try:
        x  = int(input("Enter Integer: "))

    except:
        print("wrong")

    else:
        print("You enetered a valid integer")

    finally:
        print("Program Executed!")

    return ("")

m = print("Integer Validator")
print(validator(m))
"""


f = "samphshhle.txt"
try:
    sample = open(f, "r")
    contents  = sample.read()

except NameError:
    print("wrong name: ")

except FileNotFoundError:
    print("File not found... ")

else:
    print(contents)

finally:
    sample.close()
