#
# ps3pr3.py (Problem Set 3, Problem 3)        
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.
def rot(c, n):
    """ rotate c forward by n spots inthe alphabet if c is between 'a' to 'z' or 'A' to "Z'
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.   
    if 'a'<=c<='z':
        new=ord(c)+n
        if new>ord('z'):
            return chr(new-26)
        else:
            return chr(new)
    elif 'A'<=c<='Z':
        new=ord(c)+n
        if new>ord("Z"):
            return chr(new-26)
        else:
            return chr(new)
    else:
        return c


### Put your code for the encipher function below. ###
def encipher(s, n):
    """return a string that each element in s has been rotated by n
    """
    if len(s)==0:
        return ''
    else:
        rest=encipher(s[1:],n)
        return rot(s[0],n)+rest

# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character   
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####    
def best_word(e):
    """calculate the englishness from letter_prob for each word e
    """
    if len(e)==0:
        return 0
    else:
        rest=best_word(e[1:])
        return letter_prob(e[0])+rest
    
def rot_list(s,n):
    """" return a list that all characters are changed by n
    """
    if len(s)==0:
        return ''
    else:
        rest=rot_list(s[1:],n)
        return rot(s[0],n)+rest
    
def decipher(s):
    """ decipher a word s to the most suitbale English word
    """
    result=[[best_word(rot_list(s,x)), x] for x in range(26)]
    best=max(result)
    return rot_list(s,best[1])

