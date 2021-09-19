#
# ps3pr4.py (Problem Set 3, Problem 4)
#
def first_occur(seq,elem):
    """ return the position that elem first appears in seq
    """
    if len(seq)==0:
        return -1
    if seq[0]==elem:
        return 0
    else:
        rest=first_occur(seq[1:],elem)
        if rest==-1:
            return -1
        else:
            return rest+1
        
def last_occur(seq, elem):
    """ return the position that elem last appears in seq
    """
    if len(seq)==0:
        return -1
    if seq[-1]==elem:
        return len(seq)-1
    else:
        rest=last_occur(seq[:-1],elem)
        if rest==-1:
            return -1
        else:
            return rest
        
def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest
        
def jscore(s1, s2):
    """counts the number that the characters both appears in s1 and s2
    """
    if len(s1)==0:
        return 0
    else:
        if s1[0] in s2:
            return 1+jscore(s1[1:],rem_first(s1[0],s2))
        else:
            return jscore(s1[1:],s2)