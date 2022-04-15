# standard_library.py
"""Python Essentials: The Standard Library.
<Rachel Wofford>
<MTH 520>
<April 9, 2020>
"""
import calculator as calc
from itertools import combinations, chain

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L 
    (in that order). Try to make this one line."""
    return(min(L),max(L),sum(L)/len(L))


# Problem 2
print(" "), print("Problem 2")
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    #Check if an int is mutable
    integer1 = 4
    integer2 = integer1
    integer2 += 1
    if integer1 == integer2:
        print("An int is mutable.")
    else:
        print("An int is immutable.")
    #Check if a string is mutable
    string1 = "carrot"
    string2 = string1
    string2 += "cake"
    if string1 == string2:
        print("A string is mutable.")
    else:
        print("A string is immutable.")
    #Check if a list is mutable
    list1 = [x for x in range(1,4)]
    list2 = list1
    list2 += [3, 2, 1]
    if list1 == list2:
        print("A list is mutable.")
    else:
        print("A list is immutable.")
    #Check if a tuple is mutable
    tuple1 = (1,2)
    tuple2 = tuple1
    tuple2 += (1,) 
    if tuple1 == tuple2:
        print("A tuple is mutable.")
    else:
        print("A tuple is immutable.")
    #Check if a set is mutable
    set1 = {1,2,3}
    set2 = set1
    set2.update([4,5])
    if set1 == set2:
        print("A set is mutable.")
    else:
        print("A set is immutable.")
        


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        c: The length of the triangle's hypotenuse.
    """
    a_squared = calc.product(a,a)
    b_squared = calc.product(b,b)
    c_squared = calc.sum(a_squared, b_squared)
    c = calc.sqrt(c_squared)
    return(c)
    


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    A_list = list(A)
    sets=chain.from_iterable(combinations(A_list, n) for n in range(len(A_list)+1))
    return list(sets)


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    
if __name__=='__main__':
    #Call the function for Problem 2
    prob2()