#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# ps2pr3.py - Problem Set 2, Problem 3
#
def move_to_end(s, n):
    """ this function is trying to rearrange the first n characters to the end of string s
    where s is a string and n is an integer 
    """
    first=s[0:n]
    return s[n:] + first

def reverse_last(vals, n):
    """ this function is trying to reverse the last n characters from vals
    """
    if len(vals)<=n:
        return vals[::-1]
    else:
        old=vals[0:len(vals)-n]
        new=vals[-1:len(vals)-n-1:-1]
    return old+new
