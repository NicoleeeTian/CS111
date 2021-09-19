#
# ps4pr1.py (Problem Set 4, Problem 1)        
#
def dec_to_bin(n):
    """ this functin is trying to convert a non-negative integer from decimal to binary
    the input is a non-negative intger 
    """
    if n==1:
        return str(n)
    elif n==0:
        return str(n)
    else:
        if n%2!=0:
            return dec_to_bin(n>>1)+str(1)
        else:
            return dec_to_bin(n>>1)+str(0)

def bin_to_dec(n):
    """this functin is trying to convert a non-negative integer from binary to decimal
    the input is a non-negative intger which only contains 1 and 0
    """
    if n=='0':
        return 0
    elif n=='1':
        return 1
    else:
        if n[0]=='1':
            return bin_to_dec(n[1:])+(1<<(len(n)-1))
        else:
            return bin_to_dec(n[1:])
 

