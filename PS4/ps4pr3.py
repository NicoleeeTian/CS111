#
# ps4pr3.py (Problem Set 4, Problem 3)        
#
#Funtion 1
def bitwise_and(b1,b2):
    """ return a string which represents each bit in the numbers in AND operator fron right to left
the inputs should be two strings which represents binary numbers
    """
    if len(b1)==len(b2)==0:
        return ''
    elif len(b1)==0 and len(b2)!=0:
        return len(b2)*'0'
    elif len(b2)==0 and len(b1)!=0:
        return len(b1)*'0'
    else:
        rest_bit=bitwise_and(b1[:-1],b2[:-1])
        if b1[-1]=='0' or b2[-1]=='0':
            return rest_bit+'0'
        else:
            return rest_bit+'1'

#Function 2
def add_bitwise(b1,b2):
    """ return the sum of two binary numbers
the inputs are two strings which represents binary numbers
    """
    if len(b1)==0:
        return b2
    elif len(b2)==0:
        return b1
    else:
        if b1[-1]==b2[-1]=='0':
            return add_bitwise(b1[:-1],b2[:-1])+'0'
        elif b1[-1]==b2[-1]=='1':
            return add_bitwise(add_bitwise(b1[:-1],b2[:-1]),'1')+'0'
        else:
            return add_bitwise(b1[:-1],b2[:-1])+'1'