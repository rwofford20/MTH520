# python_intro.py
"""Python Essentials: Introduction to Python.
Rachel Wofford
MTH 520
April 22, 2022
"""

#Problem 1
def isolate(a, b, c, d, e):
    """Prints the first 3 arguments separated by 5 spaces and the 
    remaining arguments separated by 1 space."""
    print(a,b,c,sep="     ", end=" "),print(d,e)
    return

#Problem 2
def first_half(string):
    half_length = round(len(string)/2)
    return string[:half_length]


def backward(first_string):

    raise NotImplementedError("Problem 2 Incomplete")

#Problem 3
def list_ops():

    raise NotImplementedError("Problem 3 Incomplete")

#Problem 4
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    raise NotImplementedError("Problem 4 Incomplete")



def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    raise NotImplementedError("Problem 5 Incomplete")

def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    raise NotImplementedError("Problem 6 Incomplete")

def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    raise NotImplementedError("Problem 7 Incomplete")


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    raise NotImplementedError("Problem 8 Incomplete")
    
if __name__=='__main__':
    #Call the function for Problem 1
    isolate(1,2,3,4,5)
    
    #Call the function for Problem 2
    print(first_half('carrot'))


