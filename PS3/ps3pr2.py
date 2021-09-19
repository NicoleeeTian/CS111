#
# ps3pr2.py (Problem Set 3, Problem 2)        
#
def cube_evens_lc(values):
    """ return a new list contains the cubes of even numbers
    """
    return [x**3 for x in values if x%2==0]

def cube_evens_rec(values):
    """ return a new list contains the cubes of even numbers
    """
    if len(values)==0:
        return []
    else:
        rest_val=cube_evens_rec(values[1:])
        if values[0]%2==0:
            return [values[0]**3]+rest_val
        else:
            return rest_val
        
def num_occur(c,s):
    """ return a number of times that c appears in s
    """
    l=[x for x in range(len(s)) if c==s[x]]
    return len(l)

def most_occur(c, words):
    """ return a word that contains the most num_occur of c
    """
    num=[[num_occur(c,x),x] for x in words]
    result=max(num)
    return result[1]

def price_string(cents):
    """ change cents into different measurement: dollars and cents
    the input should be an integer
    """
    d= cents//100
    c= cents%100
    if c==0:
        return str(d)+' dollars'
    else:
        return str(d)+ ' dollars and '+ str(c)+' cents'