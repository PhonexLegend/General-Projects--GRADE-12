import pickle

import os
"""
def addrec():
    L =[]
    f = open("data.dat", "+ab")
    rn = int(input("Enter rn: "))
    pr = int(input("Enter pn: ")) 
    rt = int(input("Enter rt: "))
    L = [rn, pr, rt]
    pickle.dump(L, f)
    print("R added")
    f.close()

addrec()
"""
"""
def disp():
    try:
        f = open("data.dat", "rb")
        while True:
            d = pickle.load(f)
            print(d)
    except:
        f.close()

disp()

"""
"""
def specific_rec(rno):
    try:
        f1 = open("data.dat","rb")
        while True:
            d = pickle.load(f1)
            if rno == d[0]:
                print(d)

    except:
        f1.close()

rno = int(input("Room no.: "))
specific_rec()
"""


def mod():
    roll = int(input("Enter room number whose record you want to Modify:"))
    try:
        file = open("data.dat", "rb+")
        f=open("temp1.dat", "wb")
        while True:
            d = pickle.load (file)
            if roll == d [0]:
                d[1]=int(input("Enter modified price"))
                d[2]=input("Enter modified room type")
            pickle.dump(d,f)
    except:
        print("Record Updated")
        file.close()
        f.close
        os.remove("data.dat")
        os.rename("temp1.dat" "data.dat")
mod()


def delete():
    roll = int(input("Enter room number whose record you want to delete:"))

    try:
        file = open("data.dat", "rb+")
        f=open("temp1.dat", "wb")
        while True:
            d = pickle.load(file)
            if roll != d [0]:
                pickle.dump(d,f)
            else:
                found = 1
    except:
        print ("Record Deleted")
        file.close()
        f.close()
        os.remove("data.dat")
        os.rename("temp1.dat", "data.dat")
delete()