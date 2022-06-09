# drazin.py
"""Volume 1: The Drazin Inverse.
Rachel Wofford
MTH 520 
May 20, 2022
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k

# Laplace function for problem 3.
def laplacian(A):
    """Compute the Laplacian matrix of the adjacency matrix A, 
        as well as the second smallest eigenvalue.
        
        Parameters: A((n,n) ndarray): Adjacency matrix for an undirected weighted graph.
        
        Returns: L((n,n) ndarray): The Laplacian matrix of A.
    """
    D = A.sum(axis=1) #The degree of each vertes(either axis).
    return np.diag(D)-A
    

# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    conditions = 0
    
    # Check if the first condition holds
    if np.allclose(A@Ad,Ad@A):
        conditions += 1
    
    # Check if the second condition holds
    if np.allclose(np.linalg.matrix_power(A, k+1)@Ad, np.linalg.matrix_power(A, k)):
        conditions += 1
    
    # Check if the third condition holds
    if np.allclose(Ad@A@Ad, Ad):
        conditions += 1
    
    # If all conditions hold return true, otherwise return false
    if conditions == 3:
        return True
    else:
        return False

# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    n = len(A[:])
    # Sort the Schur decomposition with 0 eigenvalues last
    f1 = lambda x: abs(x) > tol
    T1, Q1, k1 = la.schur(A, sort=f1)
    
    # Sort the Schur decomposition with 0 eigenvalues first
    f2 = lambda x: abs(x) <= tol
    T2, Q2, k2 = la.schur(A, sort=f2)
    
    # Create change of basis matrix 
    U = np.hstack((Q1[:,:k1], Q2[:,:n-k1]))
    
    # Find the block diagonal matrix
    V = la.inv(U)@A@U
    Z = np.zeros((n,n))
    if k1 != 0:
        Minv = la.inv(V[:k1, :k1])
        Z[:k1,:k1] = Minv
    return U@Z@la.inv(U)
    

# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    
    # Determine n and prepare to calculate R
    n = len(A[:])
    R = np.zeros((n,n), dtype=np.float)
    I = np.eye(n)
    
    for i in range(n):
        # Calculate the Laplacian of A
        L = laplacian(A)

        # Replace the ith row of the Laplacian with the ith row of the identity matrix
        L[i,:]=I[i,:]
        #print(L)
        # Calculate the Drazin inverse
        D = drazin_inverse(L, tol=1e-4)
        # Change the values according to equation 14.4 if i !=j
        for j in range(n):
            if i != j:
                R[j,i] = D[j,j]
    return R


if __name__=='__main__':
    # Test cases for Problem 1
    A = np.array([[1,3,0,0], [0,1,3,0], [0,0,1,3], [0,0,0,0]])
    Ad = np.array([[1,-3,9,81],[0,1,-3,-18],[0,0,1,3],[0,0,0,0]])
    k1 = 1
    #print(is_drazin(A, Ad, k1))
    B = np.array([[1,1,3],[5,2,6],[-2,-1,-3]])
    Bd = np.array([[0,0,0],[0,0,0],[0,0,0]])
    k2 = 3
    #print(is_drazin(B, Bd, k2))
    
    # Test case for Problem 2
    #print(drazin_inverse(A, tol=1e-4))
    
    # Test case for Problem 3
    #print(effective_resistance(A))