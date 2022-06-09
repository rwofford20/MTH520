# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
Rachel Wofford
MTH 520 
May 2022
"""
import cvxpy as cp
import numpy as np

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Initialize the objective
    x = cp.Variable(3, nonneg = True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c.T @ x)
    
    # Write the constraints
    A = np.array([1,2,0])
    G = np.array([0,1,-4])
    H = np.array([2,10,3])
    P = np.eye(3)
    constraints = [A @ x <= 3, G @ x <= 1, H @ x >= 12, P @ x >= 0]
    
    # Assemble and solve the problem
    problem = cp.Problem(objective, constraints)
    opt_value = problem.solve()
    optimizer = x.value
    
    return optimizer, opt_value

# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Initialize the objective
    x = cp.Variable(len(A.T))
    objective = cp.Minimize(cp.norm(x,1))
    
    # Write the constraints
    constraints = [A @ x == b]
    
    # Assemble and solve the problem
    problem = cp.Problem(objective, constraints)
    opt_value = problem.solve()
    optimizer = x.value
    
    return optimizer, opt_value

# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Create the system of constraints
    A = np.array([[1, 1, 0, 0, 0, 0], 
                 [0, 0, 1, 1, 0, 0], 
                 [0, 0, 0, 0, 1, 1], 
                 [-1, 0, -1, 0, -1, 0],
                 [0, -1, 0, -1, 0, -1]])
    b = np.array([7, 2, 4, -5, -8]).T
    
    # Initialize the objective
    x = cp.Variable(len(A.T), nonneg = True)
    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(x.T @ c)
    
    # Write the constraints
    constraints = [A @ x <= b]
    
    # Assemble and solve the problem
    problem = cp.Problem(objective, constraints)
    opt_value = problem.solve()
    optimizer = x.value
    
    return optimizer, opt_value
    
# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Initialize matrix Q and vector r
    Q = np.array([[3, 2, 1],[2, 4, 2], [1, 2, 3]])
    r = np.array([3, 0, 1])
    
    # Initialize the objective 
    x = cp.Variable(3)
    
    # Assemble and solve the problem
    problem = cp.Problem(cp.Minimize(0.5 * cp.quad_form(x, Q) + r.T @ x))
    opt_value = problem.solve()
    optimizer = x.value
    
    return optimizer, opt_value

# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Initialize the objective
    x = cp.Variable(len(A.T), nonneg = True)
    objective = cp.Minimize(cp.norm(A @ x - b, 2))
    
    # Write the constraints
    constraints = [cp.sum(x) == 1]
    
    # Assemble and solve the problem
    problem = cp.Problem(objective, constraints)
    opt_value = problem.solve()
    optimizer = x.value
    
    return optimizer, opt_value


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    # Optional!
    raise NotImplementedError("Problem 6 Incomplete")

if __name__=="__main__":
    # Testing problem 1
    #print(prob1())
    
    # Testing problem 2
    A = np.array([[1, 2, 1, 1], [0, 3, -2, -1]])
    b = np.array([7,4]).T
    #print(l1Min(A,b))
    
    # Testing problem 3
    #print(prob3())
    
    # Testing problem 4
    #print(prob4())
    
    # Testing problem 5
    #print(prob5(A, b))