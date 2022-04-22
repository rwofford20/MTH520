# python_intro.py
"""Python Essentials: Introduction to Python.
<Rachel Wofford>
<MTH 520>
<April 8, 2022>
"""
import numpy as np

#Problem 1 - Calculate the volume of a sphere.
print("Problem 1")
pi = 3.14159
a = 4/3  #Constant used in the volume equation  
r = 10   #The radius of the sphere
V= a * pi * r **3  #Equation for calculating the volume of a sphere
print("The volume of a sphere with radius 10 is: ", V)


#Problem 2 - Set up the Python file. 
print(" "),print("Problem 2")
print("Hello, world!") #Print a string to the terminal window
#I checked that this executed from the terminal, not sure how to show that here

#Problem 3 - Calculate the volume of a sphere using a function.
def sphere_volume(r):
    """Return the volume of a sphere of radius r. The input is r. 
    Note: The constants a and pi are defined in probem 1."""
    V = a * pi * r**3  
    return V
    

#Problem 4 - Matrix multiplication in NumPy.
def prob4():
    """Return the product of two matrices A and B."""
    A = np.array([[3, -1, 4],[1, 5, -9]])
    B = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    AB = np.dot(A,B)  #Could also us (A @ B) for matrix multiplication
    return AB
    
#Problem 5 - Calculating tax liability based on income.
def tax_liability(i):
    """Returns a person's tax liability based on their income according to the
    progressive tax system."""
    if i > 40125:  #Executes if income is over $40125
        bracket1 = 987.5  #First $9875 taxed at 10%
        bracket2 = 3630   #Next $30249.99 taxed at 12%
        bracket3 = (i - 40125.01)*.22  #Remaining income taxed at 22%
        liability = bracket1+bracket2+bracket3  
        #print("Tax liability: ", round(liability,2))
    elif i > 9875: #Executes if income is between 9875.01 and 40125 (inclusive)
        bracket1 = 987.5  #First $9875 taxed at 10%
        bracket2 = (i - 9875)*.12  #Remmaining income taxed at 12%
        liability = bracket1+bracket2
        #print("Tax liability: ", round(liability,2))
    elif i>= 0:  #Executes if income is $9875 or less
        bracket1 = i * 0.10  #Income taxed at 10%
        liability = bracket1
        #print("Tax liability: ", round(liability, 2))
    else: 
        liability = 0
    return liability


#Problem 6 - Matrix operations using NumPy and lists.
def prob6a():
    """Returns A*B, A+B, and 5A for two lists A and B defined using list comprehension."""
    A = [x for x in range(1,8)]
    B = [5 for x in range(1,8)]
    #Create empty lists to store information
    #ATB id for A*B, APB is for A+B, FA is for 5A, AB is for A*B
    ATB, APB, FA = [0 for x in range(1,8)], [0 for x in range(1,8)], [0 for x in range(1,8)]
    AB=0
    for i in range(7):
        #Perform componentwise multiplication then sum the terms for A*B
        ATB[i]=A[i]*B[i]
        AB = AB+ATB[i]
        #Perform componentwise addition for A+B
        APB[i] = A[i]+B[i]
        #multiply each term of lsi A by 5 for 5A
        FA[i]=5*A[i]
    return(AB, APB, FA)

def prob6b(): 
    """Returns A*B, A+B, and 5A for two lists A and B defined as NumPy arrays."""
    A = np.array([1, 2, 3, 4, 5, 6, 7])
    B = np.array([5, 5, 5, 5, 5, 5, 5])
    return(A@B, A+B, 5*A)

if __name__=='__main__':
    print(" "),print("Problem 3")
    #Define a radius and call the function for problem 3.
    radius = 32;
    print("The volume of a sphere with radius ", radius, " is: ", sphere_volume(radius))
    
    print(" "),print("Problem 4")
    #Call the function for problem 4.
    print("AB = ", prob4())
    
    print(" "),print("Problem 5")
    #Define an income and call the function for problem 5.
    income = 63000
    print('Tax liability: ', round(tax_liability(income),2))
    
    print(" "),print("Problem 6")
    #Call both functions for problem 6
    print("Using lists: ", prob6a())
    print("Using NumPy: ", prob6b())
    

        
    
    
    
    
    
    
    
    
    
    
    