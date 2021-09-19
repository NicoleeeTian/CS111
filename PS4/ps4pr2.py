#
# ps4pr2.py (Problem Set 4, Problem 2)        
#
from ps4pr1 import *

def mul_bin(b1, b2):
    """ this function is trying to multiply two binary numbers and return its result as a string
    the inputs are two strings which represents binary numbers
    """
    n1= bin_to_dec(b1)
    n2= bin_to_dec(b2)
    d = n1 * n2
    b = dec_to_bin(d)
    return b

def add_bytes(b1,b2):
    """ this function is trying to add two binary numbers and return its result which exactly contains 8 bit binary numbers
    the inputs should be two strings which represents binary numbers
    """
    n1= bin_to_dec(b1)
    n2= bin_to_dec(b2)
    sum_bin = dec_to_bin(n1+n2)
    if len(sum_bin)>8:
        return sum_bin[-8:]
    elif len(sum_bin)<8:
        return (8-len(sum_bin)) * '0' + sum_bin
    else:
        return sum_bin