#主函数

#import modules
import random

#main function
def selecttion():
    #Welcome User and show program name: An Optimal Sample Selection System
    print("Welcome to the An Optimal Sample Selection System")

    #prompt user to enter m 45<=m<=54, randomly generate m if no input
    m = input("Please enter the m samples number (45<=m<=54): ")
    if m == "":
        m = random.randint(45, 54)
    if m < 45 or m > 54 :
        return "Error: m must be between 45 and 54"
    m = int(m)
    
    #prompt user to enter n 7<=m<=25, randomly generate m if no input
    n = input("Please enter the n samples number (7<=n<=25): ")
    if n == "":
        n = random.randint(7, 25)
    if n < 7 or n > 25 :
        return "Error: n must be between 7 and 25"
    n = int(n)

    #prompt user to enter k 4<=k<=7, randomly generate m if no input
    k = input("Please enter the k samples number (4<=k<=7): ")
    if k == "":
        k = random.randint(4, 7)
    if k < 4 or k > 7 :
        return "Error: k must be between 4 and 7"
    k = int(k)

    #prompt user to enter s 3<=j<=7, randomly generate m if no input
    s = input("Please enter the s samples number (3<=s<=7): ")
    if s == "":
        s = random.randint(3, 7)
    if s < 3 or s > 7 :
        return "Error: s must be between 3 and 7"
    s = int(s)

    #prompt user to enter j s<=j<=k, randomly generate m if no input
    j = input("Please enter the j samples number (s<=j<=k): ")
    if j == "":
        j = random.randint(s, k)
    if j < s or j > k :
        return "Error: j must be between s and k"
    j = int(j)
    
    #Create union set
    u_set = {"null", "empty"}
    u_set.clear()
    for i in range(1, 54):
        u_set.add(i)
    
    #randomly select m samples from union set
    m_set = set(random.sample(u_set, m))
    #randomly select n samples from m set
    n_set = set(random.sample(m_set, n))
    print("n set: ", n_set)
