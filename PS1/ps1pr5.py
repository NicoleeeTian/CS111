# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions with numeric inputs
#

def last_first(values):
    """return a list contains the first and last values from the original one
    """
    last = values[-1]
    first = values[0]
    return [last, first]

def every_other(values):
    """return a list only contains the odd nums from the original one
    """
    x = values[0::2]
    return x

def begins_with(word,prefix):
    """return True if word begins with prefix
    """
    i = len(word)
    j = len(prefix)
    if i>=j:
        if word[0:j]== prefix:
            return True
        # I did not write else return False before
        else:
            return False
    else:
        return False