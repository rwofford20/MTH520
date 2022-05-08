# python_intro.py
"""Python Essentials: Introduction to Python.
Rachel Wofford
MTH 520
April 22, 2022
"""
from math import floor 
import numpy as np

#Problem 1
def isolate(a, b, c, d, e):
    """Prints the first 3 arguments separated by 5 spaces and the 
    remaining arguments separated by 1 space."""
    print(a,b,c,sep="     ", end=" "),print(d,e)
    return

#Problem 2
def first_half(string):
    """Returns the first half of parameter 'string', excluding the middle character 
    if there is an odd number of characters."""
    half_length = floor(len(string)/2)
    return string[:half_length]


def backward(first_string):
    """Returns parameter 'first_string' with the order of its characters reversed."""
    new_string = ''
    for i in range(len(first_string)):
        new_string += first_string[-i-1]
    return new_string
    

#Problem 3
def list_ops():
    """Defines a list, performs manipulations, and returns the resulting list."""
    #Define the list
    my_list = ['bear', 'ant', 'cat', 'dog']
    #Append 'eagle'
    my_list.append('eagle')
    #Replace the entry at index 2 with 'fox
    my_list[2]='fox'
    #Remove the entry at index 1
    my_list.pop(1)
    #Sort the list in reverse alphabetical order
    my_list.sort()
    my_list.reverse()
    #Replace 'eagle with 'hawk
    k = my_list.index('eagle')
    my_list[k]='hawk'
    #Add 'hunter to the last entry in the list
    my_list[-1] = my_list[-1] + 'hunter'
    
    return my_list
    

#Problem 4
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    harmonic_sum = sum([(1/i)*((-1)**(i+1)) for i in range (1,n+1)])
    return harmonic_sum
    



def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob5(A)
        array([0, 0, 3])
    """
    B = np.copy(A)
    mask = B < 0
    B[mask] = 0
    return B

def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    #Define the matrices A,B, and C
    A = (np.arange(6).reshape(3,2)).T
    B = np.tril(np.full((3,3),3), -1)+np.diag([3,3,3])
    C = np.diag([-2, -2, -2])
    #Stack each column of the block matrix
    col1 = np.vstack((np.zeros((3,3)), A, B))
    col2 = np.vstack((A.T, np.zeros((5,2))))
    col3 = np.vstack((np.eye(3), np.zeros((2,3)), C))
    #Stack the columns together horizontally
    block_matrix = np.hstack((col1,col2,col3))
    return block_matrix

def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    #Use broadcasting by adding an extra dimension
    A = A/A.sum(axis=1)[:,np.newaxis]
           
    return A


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    #No file "grid.npy" is available from PythonEssentials
    
if __name__=='__main__':
    #Call the function for Problem 1
    isolate(1,2,3,4,5)
    
    #Call the function for Problem 4 to approximate ln(2) to 5 decimal places
    print(alt_harmonic(500000))
    
    #Define a matrix a call the function for Problem 7
    A = np.array([[1,1,0],[0,1,0],[1,1,1]])
    print(prob7(A))
    


