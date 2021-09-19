#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# 
def repeat(s, n):
    """ this function is trying to repeat string s for n times
    while s is a string and n is an integer
    """
    if n<=0:
        return ''
    else:
        left=repeat(s, n-1)
        return s + left
    
def contains(s, c):
    """ this function is trying to distinguish whether s contains c
    """
    if len(s)==0:
        return False
    else:
        if s[0]==c:
            return True
        else:
            left=contains(s[1:], c)
            return left

def add(vals1, vals2):
    """this function is trying to add each number inside vals1 and vals2,
    where vals1 and vals2 are both lists contains numbers
    """
    if len(vals1)!= len(vals2):
        return []
    if len(vals1)==len(vals2)==0:
        return []
    else:
        result=vals1[0]+vals2[0]
        rest_list=add(vals1[1:], vals2[1:])
        return [result]+rest_list
