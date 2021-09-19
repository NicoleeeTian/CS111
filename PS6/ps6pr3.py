#
# ps6pr3.py - Problem Set 6, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

def add_spaces(s):
    """ this function returns a new string s which adding a pace between between each adjacent characters
    the input is string that is not empty
    """
    new_s=''
    for i in range(len(s)-1):
        new_s += s[i]+' '
    return new_s + s[-1]

def merge(s1,s2):
    """ this function return a string merge every element appears in s1 and s2
    the inputs and outputs are strings
    """
    result=''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        if s1[i]==s2[i]:
            result+=s1[i]
        else:
            result+=s1[i]+s2[i]
    return result+s1[len_shorter:]+s2[len_shorter:]

def contains(s,c):
    """ this function tests whether s contains an element c
    both inputs are string
    """
    for i in s:
        if i==c:
            return True
    return False