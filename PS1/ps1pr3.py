# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
#function1
def root(x):
    """ returns the root of its put
        input x: any number (int or float)
    """
    return x**0.5    
    
def gap(num1, num2):
    """returns the difference between num1 and num2
       inputs num1 and num2: any number (int or float)
    """
    if num1 >= num2:
        return num1-num2
    else:
        return num2-num1
    
def larger_gap(a1, a2, b1, b2):
    """ returns the larger difference between the absolute length of a1 and a2 and the absolute length of b1 and b2
        inputs a1, a2, b1, b2: any number (int or float)
    """
    if a1>=a2:
        gap1=a1-a2
    else:
        gap1=a2-a1
    if b1>=b2:
        gap2=b1-b2
    else:
        gap2=b2-b1
    if gap1>=gap2:
        return gap1
    else:
        return gap2

def median(a, b, c):
    """ returns the median number among a b and c
        inputs a, b, c: any number (int or float)
    """
    if b<=a<=c or c<=a<=b:
        return a
    elif a<=b<=c or c<=b<=a:
        return b
    else:
        return c


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
