#import modules
import random

def select():
    #Welcome User and show program name: An Optimal Sample Selection System
    print("Welcome to the An Optimal Sample Selection System")

    #Create union set
    u_set = {"null", "empty"}
    u_set.clear()
    for i in range(1, 54):
        u_set.add(i)

    #prompt user to enter m 45<=m<=54, randomly generate m if no input
    m = input("Please enter the m samples number (45<=m<=54): ")
    if m == "":
        m = random.randint(45, 54)
    if m < 45 or m > 54 :
        return "Error: m must be between 45 and 54"
    else:
        m = int(m)
    
