#
# ps6pr3.py - Problem Set 6, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#
def log(b,n):
    """ this funtion returns the logarithm to the bast b of a number n
    """
    total=0
    while n>1:
        save=n
        n//=b
        total+=1
        print('dividing',save,'by',b,'gives',n)
    return total

def add_powers(m,n):
    """ this function returns a sum the first m powers of n from 0 to m-1
    """
    total=0
    x=0
    while x<m:
        print(n,"**",x,"=", n**x)
        total+=n**x
        x+=1
    return total

def negate_odds(values):
    """ this function returns a modified list which odd-valued elements change to negative,
    """
    for i in range(len(values)):
        if values[i]%2!=0:
            values[i]= -values[i]
